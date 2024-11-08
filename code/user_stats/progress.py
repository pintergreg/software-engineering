import sqlite3
import timeit


def query_progress(user_id: int) -> float:
    # establish connection
    con = sqlite3.connect("data.db")
    # build query
    progress_query = f"""
    SELECT
        lesson / 50.0 AS progress
    FROM activity
    WHERE
        user_id = {user_id} AND
        result = 'success'
    ORDER BY
        lesson DESC
    LIMIT 1
    ;
    """
    # execute query
    res = con.execute(progress_query)
    progress = res.fetchone()[0]
    return progress


if __name__ == "__main__":
    print(query_progress(42))
    start_time = timeit.default_timer()
    query_progress(42)
    print(timeit.default_timer() - start_time)
