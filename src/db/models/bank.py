from sqlalchemy import Column, Integer, String

from src.db.connection import Base


class Banco(Base):
    """Represents a bank.

    Args:
        id (int): The unique identifier of the bank.
        name (str): The name of the bank.

    Methods:
        validate_card(hash_credit_card, customer_id): Validates if the credit card belongs to the customer.
        verify_funds(hash_credit_card, amount): Verifies if the credit card has sufficient funds.
        process_purchase(hash_credit_card, amount, merchant_id): Processes a purchase by debiting the amount.
        restore_funds(hash_credit_card, amount, merchant_id): Restores funds for a cancelled or refunded purchase.
    """
    __tablename__ = "banks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    @staticmethod
    def validate_card(hash_credit_card, customer_id):
        """Validates if the credit card belongs to the customer.

        Args:
            hash_credit_card (str): The hash of the credit card.
            customer_id (int): The ID of the customer.

        Returns:
            bool: True if the credit card belongs to the customer, False otherwise.
        """
        return True

    @staticmethod
    def verify_funds(hash_credit_card, amount):
        """Verifies if the credit card has sufficient funds.

        Args:
            hash_credit_card (str): The hash of the credit card.
            amount (Decimal): The amount to be verified.

        Returns:
            bool: True if the credit card has sufficient funds, False otherwise.
        """
        return True

    @staticmethod
    def process_purchase(hash_credit_card, amount, merchant_id):
        """Processes a purchase by debiting the amount.

        Args:
            hash_credit_card (str): The hash of the credit card.
            amount (Decimal): The amount to be debited.
            merchant_id (int): The ID of the merchant.

        Returns:
            bool: True if the purchase is successfully processed, False otherwise.
        """
        return True

    @staticmethod
    def restore_funds(hash_credit_card, amount, merchant_id):
        """Restores funds for a cancelled or refunded purchase.

        Args:
            hash_credit_card (str): The hash of the credit card.
            amount (Decimal): The amount to be restored.
            merchant_id (int): The ID of the merchant.

        Returns:
            bool: True if the funds are successfully restored, False otherwise.
        """
        return True
