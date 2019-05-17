from cryptography.utils import utils


class RSA(object):
    def __init__(self, key_digits_number):
        self.digits_amount = key_digits_number
        self.p = None
        self.q = None
        self.n = None
        self.m = None
        self.e = None
        self.d = None

    def build_private_keys(self):
        self.p = utils.build_prime_number_from_digits_amount(self.digits_amount)
        self.q = utils.build_random_prime_from_interval(
            10 ** self.digits_amount * 2, 10 ** self.digits_amount * 3)

    def build_n_value(self):
        self.n = self.p * self.q

    def build_public_keys(self):
        self.m = self.p * self.q
        self.e = utils.get_relative_prime(self.n)

    def build_decrypt_key(self):
        module = utils.get_exponent_for_decrypt(self.n)
        self.d = utils.get_powers_in_module(self.e, module, self.n)
