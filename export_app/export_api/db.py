# -*- coding: utf-8 -*-
from sqlalchemy import text
from export_app.app import db


def get_all_scored_data_rows():
    scored_data = db.session.execute(text("SELECT * FROM scored_data;")).fetchall()
    # scored_data_headers = db.session.execute(
    #     text("SELECT column_name FROM information_schema.columns WHERE table_name='scored_data';")).fetchall()
    scored_data_info = db.session.execute(text("PRAGMA table_info(scored_data);")).fetchall()
    scored_data_list = []
    # header_names = [header_t[0] for header_t in scored_data_headers]
    # scored_data_list.append(tuple(header_names))
    for row in scored_data:
        scored_data_list.append(row)
    return scored_data_list
