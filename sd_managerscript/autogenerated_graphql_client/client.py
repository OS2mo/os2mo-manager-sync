from uuid import UUID

from .async_base_client import AsyncBaseClient
from .create_manager import CreateManager
from .create_manager import CreateManagerManagerCreate
from .current_managers import CurrentManagers
from .current_managers import CurrentManagersManagers
from .engagements import Engagements
from .engagements import EngagementsEngagements
from .input_types import AssociationTerminateInput
from .input_types import ManagerCreateInput
from .input_types import ManagerTerminateInput
from .input_types import ManagerUpdateInput
from .leder_org_units import LederOrgUnits
from .leder_org_units import LederOrgUnitsOrgUnits
from .manager_engagements import ManagerEngagements
from .manager_engagements import ManagerEngagementsOrgUnits
from .org_unit_level import OrgUnitLevel
from .org_unit_level import OrgUnitLevelOrgUnits
from .root_manager_engagements import RootManagerEngagements
from .root_manager_engagements import RootManagerEngagementsOrgUnits
from .terminate_association import TerminateAssociation
from .terminate_association import TerminateAssociationAssociationTerminate
from .terminate_manager import TerminateManager
from .terminate_manager import TerminateManagerManagerTerminate
from .update_manager import UpdateManager
from .update_manager import UpdateManagerManagerUpdate


def gql(q: str) -> str:
    return q


class GraphQLClient(AsyncBaseClient):
    async def root_manager_engagements(
        self, uuid: UUID
    ) -> RootManagerEngagementsOrgUnits:
        query = gql(
            """
            query RootManagerEngagements($uuid: UUID!) {
              org_units(filter: {uuids: [$uuid]}) {
                objects {
                  validities {
                    uuid
                    has_children
                    managers {
                      uuid
                      employee {
                        engagements {
                          org_unit {
                            name
                            uuid
                            parent {
                              name
                              uuid
                            }
                          }
                          validity {
                            from
                            to
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
            """
        )
        variables: dict[str, object] = {"uuid": uuid}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return RootManagerEngagements.parse_obj(data).org_units

    async def manager_engagements(self, uuid: UUID) -> ManagerEngagementsOrgUnits:
        query = gql(
            """
            query ManagerEngagements($uuid: UUID!) {
              org_units(filter: {parent: {uuids: [$uuid]}}) {
                objects {
                  validities {
                    uuid
                    has_children
                    managers {
                      uuid
                      employee {
                        engagements {
                          org_unit {
                            name
                            uuid
                            parent {
                              name
                              uuid
                            }
                          }
                          validity {
                            from
                            to
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
            """
        )
        variables: dict[str, object] = {"uuid": uuid}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return ManagerEngagements.parse_obj(data).org_units

    async def leder_org_units(self) -> LederOrgUnitsOrgUnits:
        query = gql(
            """
            query LederOrgUnits {
              org_units(filter: {query: "_leder"}) {
                objects {
                  validities {
                    uuid
                    name
                    associations {
                      uuid
                      employee_uuid
                      org_unit_uuid
                      association_type_uuid
                      validity {
                        from
                        to
                      }
                    }
                    parent {
                      uuid
                      name
                      parent_uuid
                      org_unit_level_uuid
                    }
                  }
                }
              }
            }
            """
        )
        variables: dict[str, object] = {}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return LederOrgUnits.parse_obj(data).org_units

    async def engagements(self, uuid: UUID) -> EngagementsEngagements:
        query = gql(
            """
            query Engagements($uuid: UUID!) {
              engagements(
                filter: {employee: {uuids: [$uuid], from_date: null, to_date: null}}
              ) {
                objects {
                  validities {
                    org_unit_uuid
                    validity {
                      from
                      to
                    }
                  }
                }
              }
            }
            """
        )
        variables: dict[str, object] = {"uuid": uuid}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return Engagements.parse_obj(data).engagements

    async def current_managers(self) -> CurrentManagersManagers:
        query = gql(
            """
            query CurrentManagers {
              managers {
                objects {
                  current {
                    uuid
                    employee_uuid
                    org_unit_uuid
                  }
                }
              }
            }
            """
        )
        variables: dict[str, object] = {}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return CurrentManagers.parse_obj(data).managers

    async def org_unit_level(self, uuids: UUID) -> OrgUnitLevelOrgUnits:
        query = gql(
            """
            query OrgUnitLevel($uuids: UUID!) {
              org_units(filter: {uuids: [$uuids]}) {
                objects {
                  validities {
                    uuid
                    name
                    org_unit_level_uuid
                    parent {
                      uuid
                      org_unit_level_uuid
                    }
                  }
                }
              }
            }
            """
        )
        variables: dict[str, object] = {"uuids": uuids}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return OrgUnitLevel.parse_obj(data).org_units

    async def create_manager(
        self, input: ManagerCreateInput
    ) -> CreateManagerManagerCreate:
        query = gql(
            """
            mutation CreateManager($input: ManagerCreateInput!) {
              manager_create(input: $input) {
                uuid
              }
            }
            """
        )
        variables: dict[str, object] = {"input": input}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return CreateManager.parse_obj(data).manager_create

    async def update_manager(
        self, input: ManagerUpdateInput
    ) -> UpdateManagerManagerUpdate:
        query = gql(
            """
            mutation UpdateManager($input: ManagerUpdateInput!) {
              manager_update(input: $input) {
                uuid
              }
            }
            """
        )
        variables: dict[str, object] = {"input": input}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return UpdateManager.parse_obj(data).manager_update

    async def terminate_manager(
        self, input: ManagerTerminateInput
    ) -> TerminateManagerManagerTerminate:
        query = gql(
            """
            mutation TerminateManager($input: ManagerTerminateInput!) {
              manager_terminate(input: $input) {
                uuid
              }
            }
            """
        )
        variables: dict[str, object] = {"input": input}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return TerminateManager.parse_obj(data).manager_terminate

    async def terminate_association(
        self, input: AssociationTerminateInput
    ) -> TerminateAssociationAssociationTerminate:
        query = gql(
            """
            mutation TerminateAssociation($input: AssociationTerminateInput!) {
              association_terminate(input: $input) {
                uuid
              }
            }
            """
        )
        variables: dict[str, object] = {"input": input}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return TerminateAssociation.parse_obj(data).association_terminate
