from rolepermissions.roles import AbstractUserRole

class Comercial(AbstractUserRole):
	available_permissions = {'criar_metas':True, 'ver_metas': True}
		#(basicamente um dicionário de chaves, onde as chaves são as permissões, setando True ou False)

class Estoque(AbstractUserRole):
	available_permissions = {'acessar_produtos':True, 'ver_metas': True}