

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

    def send_payment_details(amount, card_info, merchant_id):
        """Sends payment details to the processing organization."""
        print(f"Processing ${amount} payment from card {card_info['card_number']} to merchant {merchant_id}")
        return {"status": "success", "transaction_id": "12345ABC"}

    def process_payment(self, card_info, amount, merchant_id):
        """Processes a payment."""
        if not self.validate_card(card_info['card_number'], card_info['expiration_date'], card_info['cvv']):
            raise ValueError("Invalid card details")

        result = self.send_payment_details(amount, card_info, merchant_id)

        if result['status'] == "success":
            print(f"Payment successful. Transaction ID: {result['transaction_id']}")
            return result
        else:
            raise Exception("Payment failed")
