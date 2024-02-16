create table audit_log
(
    id            serial
        primary key,
    user_id       integer,
    activity_type varchar   not null,
    bearer_token  varchar,
    ip_address    varchar,
    path          varchar   not null,
    timestamp     timestamp not null
);

