import os
import json
import random
import molotov
from molotov import global_setup, scenario

@global_setup()
def init_test(args):
    BASE_URL=os.getenv('BASE_URL', '')
    molotov.set_var('base_url', BASE_URL)

@scenario(weight=50)
async def _test_list_todos(session):
    base_url= molotov.get_var('base_url')
    async with session.get(base_url + '/todos') as resp:
        assert resp.status == 200, resp.status

@scenario(weight=30)
async def _test_create_todo(session):
    base_url= molotov.get_var('base_url')
    todo_data = json.dumps({'text': 'Utworzono nowy element todo podczas testu obciążenia Taurusa/molotova'})
    async with session.post(base_url + '/todos', data=todo_data) as resp:
        assert resp.status == 200

@scenario(weight=10)
async def _test_update_todo(session):
    base_url= molotov.get_var('base_url')
    # wyświetlenie listy wszystkich elementów todo
    async with session.get(base_url + '/todos') as resp:
        res = await resp.json()
        assert resp.status == 200, resp.status
        # wybór losowego elementu todo i jego aktualizacja z wykorzystaniem żądania PUT
        todo_id = random.choice(res)['id']
        todo_data = json.dumps({'text': 'Zaktualizowano istniejący element todo podczas testu obciążenia Taurusa/molotova'})
        async with session.put(base_url + '/todos/' + todo_id, data=todo_data) as resp:
            assert resp.status == 200

@scenario(weight=10)
async def _test_delete_todo(session):
    base_url= molotov.get_var('base_url')
    # list all todos
    async with session.get(base_url + '/todos') as resp:
        res = await resp.json()
        assert resp.status == 200, resp.status
        # wybranie losowego elemnetu todo i usunięcie go za pomocą żądania DELETE
        todo_id = random.choice(res)['id']
        async with session.delete(base_url + '/todos/' + todo_id) as resp:
            assert resp.status == 200

