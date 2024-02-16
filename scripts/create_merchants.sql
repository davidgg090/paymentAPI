create table merchants
(
    id                 serial
        primary key,
    name               varchar(255)                       not null,
    email              varchar(255)                       not null
        unique,
    is_active          boolean                  default true,
    amount_account     integer                  default 0 not null,
    created_at         timestamp with time zone default CURRENT_TIMESTAMP,
    updated_at         timestamp with time zone default CURRENT_TIMESTAMP,
    authentication_key varchar                            not null
        constraint merchants_unique
            unique
);

