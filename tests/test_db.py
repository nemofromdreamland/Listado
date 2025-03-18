from dataclasses import asdict

import pytest
from sqlalchemy import select

from listado.models import Todo, User


@pytest.mark.asyncio
async def test_user_todo_relationship(session, user: User):
    todo = Todo(
        title='Test Todo',
        description='Test Desc',
        state='draft',
        user_id=user.id,
    )

    session.add(todo)
    await session.commit()
    await session.refresh(user)

    user = await session.scalar(select(User).where(User.id == user.id))

    assert user.todos == [todo]


@pytest.mark.asyncio
async def test_create_todo(session, user):
    todo = Todo(
        title='Test Todo',
        description='Test Desc',
        state='draft',
        user_id=user.id,
    )

    session.add(todo)
    await session.commit()

    todo = await session.scalar(select(Todo))

    assert asdict(todo) == {
        'description': 'Test Desc',
        'id': 1,
        'state': 'draft',
        'title': 'Test Todo',
        'user_id': 1,
    }
