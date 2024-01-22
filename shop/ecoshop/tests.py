# from  unittest import TestCase
from django.test import TestCase, Client, override_settings
from base64 import b64encode
from unittest.mock import patch, MagicMock
from .models import QueueTest, Product


# sys.path.append(""C:\path\to\your\project"")


class Queue:
    FIFO = "FIFO"
    LIFO = "LIFO"
    POSSIBLE_STRATEGIES = ["FIFO", "LIFO"]

    def __init__(self, strategy="FIFO"):
        if strategy not in self.POSSIBLE_STRATEGIES:
            raise ValueError
        self.strategy = strategy

    def add(self, value):
        QueueTest.objects.create(value=value)

    def pop(self):

        if QueueTest.objects.all():
            if self.strategy == self.FIFO:
                que = QueueTest.objects.order_by("id").first()
            elif self.strategy == self.LIFO:
                que = QueueTest.objects.order_by("id").last()

            que.delete()
            return que.value
        else:
            raise ValueError


# Create your tests here.
class TestQueue(TestCase):
    def test_queue_exist(self):
        queue = Queue()
        self.assertIsInstance(queue, Queue)

    def test_set_wrong_strategy(self):
        with self.assertRaises(ValueError):
            wrong_strategy = "FIFA"
            queue = Queue(wrong_strategy)

    def test_add_value(self):
        queue = Queue("FIFO")
        first_number = 1
        queue.add(first_number)
        value = queue.pop()
        self.assertEqual(value, first_number)

    def test_add_multivalues(self):
        queue = Queue("FIFO")
        numbers = [1, 1, 4]
        for numb in numbers:
            queue.add(numb)

        for numb in numbers:
            value = queue.pop()
            self.assertEqual(value, numb)

    def test_add_multivalues_in_diff_way(self):
        queue = Queue("FIFO")
        numbers = [1, 4, 1]
        for numb in numbers:
            queue.add(numb)

        for numb in numbers:
            value = queue.pop()
            self.assertEqual(value, numb)

    def test_add_multivalues_with_solt(self):
        queue = Queue("FIFO")
        numbers = [1, 1, 4]
        for numb in numbers:
            queue.add(numb)

        for i in range(33, 37):
            queue.add(i)

        for numb in numbers:
            value = queue.pop()
            self.assertEqual(value, numb)

    def test_empty_queue(self):
        queue = Queue("FIFO")
        numb = 1
        queue.add(numb)
        value = queue.pop()
        self.assertEqual(value, numb)
        with self.assertRaises(ValueError):
            queue.pop()


class TestIndexView(TestCase):
    def test_my_index(self):
        client = Client()
        response = client.get("/ecoshop/index/")
        self.assertEqual(response.status_code, 200)


class TestModelProduct(TestCase):
    def test_create_product(self):
        name = "Melon"
        price = 5.26
        amount = 500
        category = "FR"
        name_verbose = "Название"
        name_max_length = 30
        Product.objects.create(
            name=name,
            price=price,
            amount=amount,
            category=category
        )
        product = Product.objects.all()
        self.assertEqual(len(product), 1)
        self.assertEqual(product[0].name, name)
        self.assertEqual(product[0].price, price)
        self.assertEqual(product[0].amount, amount)
        self.assertEqual(product[0].category, category)
        self.assertEqual(product[0]._meta.get_field("name").verbose_name, name_verbose)
        self.assertEqual(product[0]._meta.get_field("name").max_length, name_max_length)

    @override_settings(CELERY_TASK_ALWAYS_EAGER=True)
    @patch('ecoshop.tasks.requests')
    def test_create_product_form_view(self,fake_requests):

        img_content = b'12345678'
        fake_response = MagicMock()
        fake_requests.post.return_value = fake_response
        fake_response.json.return_value = {'images': [b64encode(img_content)]}

        client = Client()
        name = "watermelon"
        description = "good watermelon"
        price =  5.25
        amount = 900
        category = "FR"

        response = client.post("/ecoshop/create_product/",
                    {
                        'name': name,
                        'description': description,
                        'price': price,
                        'amount': amount,
                        'category': category,
                    })

        product = Product.objects.all()[0]
        # import pdb;pdb.set_trace()
        self.assertEqual(response.status_code,302)
        self.assertEqual(product.name, name)
        self.assertEqual(product.description, description)
        self.assertEqual(product.price, price)
        self.assertEqual(product.amount, amount)
        self.assertEqual(product.image.readline(),img_content)




    #
# if __name__ == '__main__':
#     unittest.main()
