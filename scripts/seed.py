import os, django
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from user.models import User, Administrator, Employee
from estate.models import ServiceContractingPlan, Estate

def create_administrator(amount):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(amount):
        username = fake.user_name()
        print('Administrator', username)
        user = User.objects.create_user(username=username, email=fake.email(), password='senha', first_name=fake.first_name(), last_name=fake.last_name())
        a = Administrator(administrator=user)
        a.save()

def create_estate(amount):
    fake = Faker('pt_BR')
    Faker.seed(11)
    for i in range(amount):
        plan = 1
        if i == 0 or i == 2:
            plan = 2
        servic_contracting_plan = ServiceContractingPlan.objects.get(id=plan)
        estate = Estate(name=fake.company(), servic_contracting_plan=servic_contracting_plan)
        estate.save()

def create_employee(amount):
    fake = Faker('pt_BR')
    Faker.seed(11)
    for i in range(amount):
        estate = Estate.objects.get(id=i+1)
        username = fake.user_name()
        print('Employee', username)
        user = User.objects.create_user(username=username, email=fake.email(), password='senha', first_name=fake.first_name(), last_name=fake.last_name())
        eg = Employee(employee=user, is_Manager=True, estate=estate)
        eg.save()
        if i == 0 or i == 2:
            for _ in range(i+2):
                username = fake.user_name()
                print('Realtor', username)
                user = User.objects.create_user(username=username, email=fake.email(), password='senha', first_name=fake.first_name(), last_name=fake.last_name())
                er = Employee(employee=user, is_Manager=False, estate=estate)
                er.realtor = eg
                er.save()

User.objects.create_superuser(username='teste_super', email='teste_super@teste.com', password='123!@#qwe', first_name='Super', last_name='User')
User.objects.create_user(username='teste', email='teste@teste.com', password='123qwe', first_name='Alone', last_name='User')

ServiceContractingPlan.objects.create(name='Básico')
ServiceContractingPlan.objects.create(name='Avançado')

create_administrator(2)
create_estate(5)
create_employee(5)