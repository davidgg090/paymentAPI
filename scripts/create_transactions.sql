create table transactions
(
    id               serial
        primary key,
    merchant_id      integer                                                       not null
        references merchants,
    customer_id      integer                                                       not null
        references customers,
    amount           numeric(10, 2)                                                not null,
    currency         char(3)                                                       not null,
    state            varchar(255)             default 'pending'::character varying not null,
    hash_credit_card varchar(255)                                                  not null,
    created_at       timestamp with time zone default CURRENT_TIMESTAMP,
    updated_at       timestamp with time zone default CURRENT_TIMESTAMP,
    token            varchar                                                       not null
        constraint transactions_unique
            unique
);
