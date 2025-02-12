from adapters.aws.SSMAdapter import SSMAdapter


class HLAuthInfo:
    def __init__(self, ssm_adapter: SSMAdapter):
        self.dob = ssm_adapter.get_param("hl-login-dob")
        self.user_name = ssm_adapter.get_param("hl-login-username")
        self.password = ssm_adapter.get_param("hl-login-password")
        self.secure_no = ssm_adapter.get_param("hl-login-secure-no")
