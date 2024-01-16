import pytest
import json
from tests import app
from core.models.assignments import Assignment, AssignmentStateEnum
from core import db


@pytest.fixture
def client():
    return app.test_client()


@pytest.fixture
def h_student_1():
    headers = {
        'X-Principal': json.dumps({
            'student_id': 1,
            'user_id': 1
        })
    }

    return headers


@pytest.fixture
def h_student_2():
    headers = {
        'X-Principal': json.dumps({
            'student_id': 2,
            'user_id': 2
        })
    }

    return headers


@pytest.fixture
def h_teacher_1():
    headers = {
        'X-Principal': json.dumps({
            'teacher_id': 1,
            'user_id': 3
        })
    }

    return headers


@pytest.fixture
def h_teacher_2():
    headers = {
        'X-Principal': json.dumps({
            'teacher_id': 2,
            'user_id': 4
        })
    }

    return headers


@pytest.fixture
def h_principal():
    headers = {
        'X-Principal': json.dumps({
            'principal_id': 1,
            'user_id': 5
        })
    }

    return headers

@pytest.fixture
def mark_assignment_as_drafted():
    assignment = Assignment.get_by_id(2)
    state, teacher_id = assignment.state, assignment.teacher_id

    # marking state and teacher as draft and null for tests
    assignment.state = AssignmentStateEnum.DRAFT
    assignment.teacher_id = None
    db.session.flush()

    yield assignment

    # reverting back to old state after test execution is completed
    assignment.state = state
    assignment.teacher_id = teacher_id
    db.session.flush()

# Fixture to roll back changes made during the test
@pytest.fixture
def rollback_changes(request):
    # Setup: Code to run before the test
    db.session.begin(subtransactions=True)
    request.addfinalizer(db.session.rollback)