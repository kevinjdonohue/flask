class TokensController:
    def get_all_tokens(self):
        tokens = {
            'httpStatusCode': '200',
            'messages': [],
            'gdsTokens': [
                {
                    'appId': 'TESTER',
                    'securityToken': 'security-token-one'
                },
                {
                    'appId': 'TESTER2',
                    'securityToken': 'security-token-two'
                }
            ]
        }

        return tokens
