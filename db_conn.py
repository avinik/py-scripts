import pymysql

from common.app_utils import app_utils


def get_cursor(db_name="fms"):
    """Get SQL cursor"""
    db_credential = app_utils.config.get('DATABASE')
    conn = pymysql.connect(
        database=db_name,
        user=db_credential["DB_USER"],
        password=db_credential.get("DB_PASSWORD"),
        host=db_credential["DB_HOST"],
    )
    cursor = conn.cursor()
    return cursor, conn


def get_mapping(cursor):
    mapping = {}
    for i, description in enumerate(cursor.description):
        mapping[description[0]] = i
    return mapping


def get_mapped_row(cursor):
    """
    Return Mapped dict
    :param cursor: sql cursor to fetch
    :return: Mapped dict
    """
    mapping = get_mapping(cursor)
    inv_mapping = {v: k for k, v in mapping.items()}
    mapped_row = {}
    res = cursor.fetchone()
    if res is None:
        return res
    for i, val in enumerate(res):
        mapped_row[inv_mapping[i]] = val
    return mapped_row


def get_mapped_rows(cursor):
    """
    Return list of mapped dict
    :param cursor: sql cursor to fetch
    :return: list of mapped dict
    """
    mapping = get_mapping(cursor)
    inv_mapping = {v: k for k, v in mapping.items()}
    res = cursor.fetchall()
    mapped_rows = []
    for row in res:
        mapped_row = {}
        for i, val in enumerate(row):
            mapped_row[inv_mapping[i]] = val
        mapped_rows.append(mapped_row)
    return mapped_rows
