create table customers
(
    id               serial
        primary key,
    name             varchar(255) not null,
    email            varchar(255) not null
        unique,
    address          varchar(255),
    hash_credit_card varchar(255) not null,
    is_active        boolean                  default true,
    created_at       timestamp with time zone default CURRENT_TIMESTAMP,
    updated_at       timestamp with time zone default CURRENT_TIMESTAMP
);

