create table tokens
(
    id           serial
        primary key,
    access_token varchar(255) not null
        unique,
    token_type   varchar(255) not null,
    created_at   timestamp with time zone default CURRENT_TIMESTAMP,
    updated_at   timestamp with time zone default CURRENT_TIMESTAMP,
    user_id      integer
        references users
);

