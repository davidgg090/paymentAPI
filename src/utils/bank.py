class BankUtils:
    """Utility class for bank operations.

    Methods:
        verify_hash_credit_card(hash_transaction, customer_hash): Verifies if
        the transaction hash matches the customer hash.
    """
    @staticmethod
    def verify_hash_credit_card(hash_transaction, customer_hash):
        """Verifies if the transaction hash matches the customer hash.

        Args:
            hash_transaction (str): The hash of the transaction.
            customer_hash (str): The hash of the customer.

        Returns:
            bool: True if the transaction hash matches the customer hash, False otherwise.
        """
        return hash_transaction == customer_hash
