import string
import random

chars_ = string.digits + string.ascii_letters


class CodeGenerator:
    @staticmethod
    def code_slug_generator(size, chars=chars_):
        return "".join(random.choice(chars) for _ in range(size))

    @staticmethod
    def code_only_numbers_generator(size, chars=string.digits):
        return "".join(random.choice(chars) for _ in range(size))

    @classmethod
    def create_user_activation_code(cls, size, model_):
        new_code = cls.code_only_numbers_generator(size=size)
        qs_exists = model_.objects.filter(activation_code=new_code).exists()
        return cls.create_user_activation_code(size, model_) if qs_exists else new_code

    @classmethod
    def create_slug_shortcode(cls, size, model_):
        new_code = cls.code_slug_generator(size=size)
        qs_exists = model_.objects.filter(activation_code=new_code).exists()
        return cls.create_slug_shortcode(size, model_) if qs_exists else new_code

    @classmethod
    def create_product_shortcode(cls, size, model_):
        new_code = cls.code_slug_generator(size=size)
        qs_exists = model_.objects.filter(code=new_code).exists()
        return cls.create_product_shortcode(size, model_) if qs_exists else new_code

    @classmethod
    def create_invoice_id(cls, size, model_):
        new_id = cls.code_slug_generator(size=size, chars=string.digits)
        id_exists = model_.objects.filter(invoice_id=new_id).exists()
        return cls.create_slug_shortcode(size, model_) if id_exists else new_id

