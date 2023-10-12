-- 01. User-defined Function Full Name.
CREATE FUNCTION fn_full_name (first_name VARCHAR, last_name VARCHAR)
RETURNS VARCHAR
AS $$
DECLARE 
	"Full Name" VARCHAR(255);

BEGIN
	"Full Name" := INITCAP(CONCAT_WS(' ', first_name, last_name));

	RETURN "Full Name";
END;

$$ LANGUAGE plpgsql;



-- 02. User-defined Function Future Value.
CREATE FUNCTION fn_calculate_future_value (initial_sum DECIMAL(20, 4), 
				yearly_interest_rate DECIMAL(10,5), number_of_years INT)
RETURNS DECIMAL(20,4)
AS $$
DECLARE
	future_value DECIMAL(20,4);

BEGIN
	RETURN TRUNC(
		initial_sum * POWER(1 + yearly_interest_rate, number_of_years), 4);
END;

$$ LANGUAGE plpgsql;



-- 03. User-defined Function Is Word Comprised.
CREATE FUNCTION fn_is_word_comprised (set_of_letters VARCHAR(50), word VARCHAR(50))
RETURNS BOOLEAN
AS $$
DECLARE 
	i INT := 1;
	char_count INT := LENGTH(word);
	lowered_set VARCHAR(50) := LOWER(set_of_letters);
	lowered_word VARCHAR(50) := LOWER(word);
	char_found BOOLEAN := TRUE;

BEGIN
	WHILE 
		i <= char_count 
		AND char_found 
	LOOP (
		WHILE 
			i <= char_count
			AND SUBSTRING(lowered_word FROM i FOR 1) !~* '[a-z]'
		LOOP
			i := i + 1;
		END LOOP;
		)
	
		IF i > char_count THEN 
			char_found := FALSE;
		END IF;

		IF POSITION(SUBSTRING(lowered_word FROM i FOR 1) IN lowered_set) = 0 THEN 
			char_found := FALSE;
		END IF;
		
		i := i + 1;
	
	END LOOP;
	
	RETURN char_found;
END;

$$ LANGUAGE plpgsql;



-- 04. Game Over.
CREATE FUNCTION fn_is_game_over (is_game_over BOOLEAN)
RETURNS TABLE (name VARCHAR(50), game_type_id INT, is_finished BOOLEAN)
AS $$

BEGIN
	RETURN QUERY
	SELECT 
		g.name,
		g.game_type_id,
		g.is_finished
	FROM 
		games g
	WHERE 
		g.is_finished = is_game_over;
END;

$$ LANGUAGE plpgsql;



-- 05. Difficulty Level. 
CREATE FUNCTION fn_difficulty_level(level INT)
RETURNS VARCHAR(50)
AS $$
DECLARE 
	difficulty_level VARCHAR(50);

BEGIN
	difficulty_level := 
		CASE 
			WHEN level <= 40 THEN 'Normal Difficulty'
			WHEN level BETWEEN 41 AND 60 THEN 'Nightmare Difficulty'
			ELSE 'Hell Difficulty'
		END;

	RETURN difficulty_level;
END;

$$ LANGUAGE plpgsql;


SELECT 
	user_id,
	"level",
	cash, 
	(fn_difficulty_level(level)) as difficutly_level
FROM 
	users_games
ORDER BY 
	user_id;



-- 06. Cash in User Games Odd Rows.
CREATE FUNCTION fn_cash_in_users_games(game_name VARCHAR(50))
RETURNS TABLE (total_cash NUMERIC)
AS $$

BEGIN
	RETURN QUERY
	SELECT
		ROUND(SUM(cash),2) AS total_cash
	FROM (
		SELECT
			ug.cash,
			ROW_NUMBER() OVER(ORDER BY ug.cash DESC) AS row_num
		FROM
			users_games ug
		JOIN games g 
			ON g.id = ug.game_id
		WHERE
			g.name = game_name
		) AS ranked
	WHERE
		row_num % 2 <> 0;
END;

$$ LANGUAGE plpgsql;



--- 07. Retrieving Account Holders.
CREATE OR REPLACE PROCEDURE sp_retrieving_holders_with_balance_higher_than(searched_balance NUMERIC)
AS $$
DECLARE 
	holder_record RECORD;
	total_balance NUMERIC;

BEGIN
	FOR holder_record IN (
		SELECT
			h.first_name,
			h.last_name
		FROM
			account_holders h
		ORDER BY
			h.first_name,
			h.last_name
		) LOOP
			SELECT
				COALESCE(SUM(a.balance), 0) INTO total_balance
			FROM
				accounts a
			WHERE
				a.account_holder_id = (
				SELECT
					id
				FROM
					account_holders
				WHERE
					first_name = holder_record.first_name
					AND last_name = holder_record.last_name
				);

			IF total_balance > searched_balance THEN 
				RAISE NOTICE 'NOTICE: % % - %', 
					holder_record.first_name, holder_record.last_name, total_balance;
			END IF;
	END LOOP;
END;

$$ LANGUAGE plpgsql;



-- 08. Deposit Money.
CREATE OR REPLACE PROCEDURE sp_deposit_money(account_id INT, money_amount NUMERIC(19,4))
AS $$

BEGIN 
	IF (
		SELECT
			COUNT(id)
		FROM
			accounts
		WHERE
			id = account_id
		) <> 1 THEN 
		ROLLBACK;
	ELSE
		UPDATE 
			accounts
		SET 
			balance = balance + money_amount
		WHERE 
			id = account_id;
	END IF;

	COMMIT;
END;

$$ LANGUAGE plpgsql;



-- 09. Withdraw Money.
CREATE OR REPLACE PROCEDURE sp_withdraw_money (account_id INT, money_amount NUMERIC(19,4))
AS $$

BEGIN 
	IF (
		SELECT
			balance
		FROM
			accounts
		WHERE
			id = account_id
		) >= money_amount
	THEN
		UPDATE 
			accounts
		SET 
			balance = balance - money_amount
		WHERE 
			id = account_id;
	ELSE
		RAISE NOTICE 'NOTICE: Insufficient balance to withdraw %', money_amount;
		ROLLBACK;
	END IF;
END;

$$ LANGUAGE plpgsql;



-- 10. Money Transfer.
CREATE OR REPLACE PROCEDURE sp_transfer_money (sender_id INT, receiver_id INT, amount NUMERIC)
AS $$

DECLARE 
	sender_balance NUMERIC;

BEGIN 
	CALL sp_withdraw_money(sender_id, amount);

	SELECT
		balance INTO sender_balance
	FROM
		accounts
	WHERE
		id = sender_id;
	
	IF sender_balance < 0 THEN
		RAISE NOTICE 'NOTICE: Insufficient balance to withdraw %', amount;
		ROLLBACK;
	END IF;

	CALL sp_deposit_money(receiver_id, amount);
END;

$$ LANGUAGE plpgsql;



-- 11. Delete Procedure.
DROP PROCEDURE sp_retrieving_holders_with_balance_higher_than;



-- 12. Log Accounts Trigger.
CREATE TABLE logs (
	id SERIAL PRIMARY KEY,
	account_id INT,
	old_sum NUMERIC(20,4),
	new_sum NUMERIC(20,4)
);


CREATE OR REPLACE FUNCTION trigger_fn_insert_new_entry_into_logs ()
RETURNS TRIGGER
AS $$

BEGIN
	INSERT INTO logs (account_id, old_sum, new_sum)
	VALUES 
		(old.id, old.balance, new.balance);

	RETURN NEW;
END;

$$ LANGUAGE plpgsql;


CREATE OR REPLACE TRIGGER tr_account_balance_change
AFTER UPDATE OF balance
	ON accounts
FOR EACH ROW
WHEN (old.balance <> new.balance)
	EXECUTE FUNCTION 
		trigger_fn_insert_new_entry_into_logs();



-- 13. Notification Email on Balance Change.
CREATE TABLE notification_emails (
	id SERIAL PRIMARY KEY,
	recipient_id INT,
	subject VARCHAR(255),
	body TEXT
);


CREATE OR REPLACE FUNCTION trigger_fn_send_email_on_balance_change ()
RETURNS TRIGGER
AS $$

BEGIN 
	INSERT INTO notification_emails (recipient_id, subject, body)
	VALUES
		(new.account_id, CONCAT('Balance change for account: ', new.account_id),
			CONCAT('On ', CURRENT_DATE, ' your balance was changed from ', old.balance, ' to ', new.balance, '.'));

	RETURN NEW;
END;

$$ LANGUAGE plpgsql;


CREATE OR REPLACE TRIGGER tr_send_email_on_balance_change
AFTER UPDATE 
	ON logs
FOR EACH ROW
EXECUTE FUNCTION 
	trigger_fn_send_email_on_balance_change();


