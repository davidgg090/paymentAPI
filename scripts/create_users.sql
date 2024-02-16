create table users
(
    id         integer                  default nextval('user_id_seq'::regclass) not null
        constraint user_pkey
            primary key,
    username   varchar(255)                                                      not null
        constraint user_username_key
            unique,
    password   varchar(255)                                                      not null
        constraint user_password_key
            unique,
    created_at timestamp with time zone default CURRENT_TIMESTAMP,
    updated_at timestamp with time zone default CURRENT_TIMESTAMP
);