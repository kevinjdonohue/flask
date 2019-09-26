from tokens_controller import TokensController


class TestTokensController:

    def test_get_all_tokens(self):
        # arrange
        expected_tokens_json = {
            'gdsTokens': [
                {
                    'appId': 'TESTER',
                    'securityToken': 'security-token-one'
                },
                {
                    'appId': 'TESTER2',
                    'securityToken': 'security-token-two'
                }
            ],
            'httpStatusCode': '200',
            'messages': []
        }

        controller = TokensController()

        # act
        actual_tokens_json = controller.get_all_tokens()

        # assert
        assert actual_tokens_json == expected_tokens_json
