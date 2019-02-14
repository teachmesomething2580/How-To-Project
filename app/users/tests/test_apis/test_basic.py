"""
필수 입력 값 / 모든 입력값 2개의 테스트 케이스로 테스트를 수행한다.
"""
import os
import shutil

from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import resolve_url
from django.test.client import encode_multipart

from base.base_test_mixins import BaseTestMixin


class TestUserBasicAPI(BaseTestMixin):

    def teardown_method(self, client):
        if os.path.exists(settings.MEDIA_ROOT):
            shutil.rmtree(settings.MEDIA_ROOT)

    def _test_create_user_api(self, client):
        context = {
            'user_id': 'user_id',
            'password': 'P@ssw0rd',
            'email': 'email@email.com',
            'nickname': 'nickname'
        }

        response = self._create_users_with_context(client, context)

        assert response.status_code == 201

        user = get_user_model().objects.get(pk=1)

        assert user.user_id == context['user_id']
        assert user.password
        assert user.email == context['email']
        return user, response

    def test_create_user_api_required_fields(self, client):
        self._test_create_user_api(client)

    def test_patch_user_api_all_fields(self, client):
        _, response = self._test_create_user_api(client)

        header = {
            'HTTP_AUTHORIZATION': 'Token ' + response.json()['token'],
        }

        context = {
            'nickname': 'first',
            'description': 'first',
            'profile_image': self._create_image(),
        }

        enc_content = encode_multipart('BoUnDaRyStRiNg', context)
        content_type = 'multipart/form-data; boundary=BoUnDaRyStRiNg'

        response = client.patch(resolve_url('users:me-profile'),
                                **header,
                                data=enc_content,
                                content_type=content_type)

        assert response.status_code == 200

        user = get_user_model().objects.get(pk=1)

        json = response.json()

        assert json.get('user_id') == 'user_id'
        assert json.get('email') == 'email@email.com'
        assert json.get('created_at')
        assert json.get('description') == context['description']
        assert json.get('nickname') == context['nickname']

        assert user.profile_image.url in json.get('profile_image')
        assert os.path.exists(os.path.join(settings.MEDIA_ROOT, user.profile_image.path))