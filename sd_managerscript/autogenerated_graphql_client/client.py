from uuid import UUID

from ._testing__create_association import TestingCreateAssociation
from ._testing__create_association import TestingCreateAssociationAssociationCreate
from ._testing__create_employee import TestingCreateEmployee
from ._testing__create_employee import TestingCreateEmployeeEmployeeCreate
from ._testing__create_engagement import TestingCreateEngagement
from ._testing__create_engagement import TestingCreateEngagementEngagementCreate
from ._testing__create_org_unit import TestingCreateOrgUnit
from ._testing__create_org_unit import TestingCreateOrgUnitOrgUnitCreate
from ._testing__get_association_type import TestingGetAssociationType
from ._testing__get_association_type import TestingGetAssociationTypeClasses
from ._testing__get_engagement_type import TestingGetEngagementType
from ._testing__get_engagement_type import TestingGetEngagementTypeFacets
from ._testing__get_job_function import TestingGetJobFunction
from ._testing__get_job_function import TestingGetJobFunctionFacets
from ._testing__get_manager_level import TestingGetManagerLevel
from ._testing__get_manager_level import TestingGetManagerLevelClasses
from ._testing__get_org_unit_level import TestingGetOrgUnitLevel
from ._testing__get_org_unit_level import TestingGetOrgUnitLevelClasses
from ._testing__get_org_unit_type import TestingGetOrgUnitType
from ._testing__get_org_unit_type import TestingGetOrgUnitTypeClasses
from .async_base_client import AsyncBaseClient
from .base_model import UNSET
from .base_model import UnsetType
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

    async def _testing__get_org_unit_type(self) -> TestingGetOrgUnitTypeClasses:
        query = gql(
            """
            query _Testing_GetOrgUnitType {
              classes(filter: {facet_user_keys: "org_unit_type"}) {
                objects {
                  uuid
                }
              }
            }
            """
        )
        variables: dict[str, object] = {}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return TestingGetOrgUnitType.parse_obj(data).classes

    async def _testing__get_org_unit_level(self) -> TestingGetOrgUnitLevelClasses:
        query = gql(
            """
            query _Testing_GetOrgUnitLevel {
              classes(filter: {facet_user_keys: "org_unit_level"}) {
                objects {
                  uuid
                }
              }
            }
            """
        )
        variables: dict[str, object] = {}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return TestingGetOrgUnitLevel.parse_obj(data).classes

    async def _testing__get_association_type(self) -> TestingGetAssociationTypeClasses:
        query = gql(
            """
            query _Testing_GetAssociationType {
              classes(filter: {facet_user_keys: "association_type"}) {
                objects {
                  uuid
                }
              }
            }
            """
        )
        variables: dict[str, object] = {}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return TestingGetAssociationType.parse_obj(data).classes

    async def _testing__get_engagement_type(self) -> TestingGetEngagementTypeFacets:
        query = gql(
            """
            query _Testing_GetEngagementType {
              facets(filter: {user_keys: "engagement_type"}) {
                objects {
                  current {
                    classes {
                      uuid
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
        return TestingGetEngagementType.parse_obj(data).facets

    async def _testing__get_manager_level(self) -> TestingGetManagerLevelClasses:
        query = gql(
            """
            query _Testing_GetManagerLevel {
              classes(filter: {facet_user_keys: "manager_level"}) {
                objects {
                  uuid
                }
              }
            }
            """
        )
        variables: dict[str, object] = {}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return TestingGetManagerLevel.parse_obj(data).classes

    async def _testing__get_job_function(self) -> TestingGetJobFunctionFacets:
        query = gql(
            """
            query _Testing_GetJobFunction {
              facets(filter: {user_keys: "engagement_job_function"}) {
                objects {
                  current {
                    classes {
                      uuid
                      user_key
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
        return TestingGetJobFunction.parse_obj(data).facets

    async def _testing__create_org_unit(
        self,
        name: str,
        org_unit_type: UUID,
        parent: UUID | None | UnsetType = UNSET,
        org_unit_level: UUID | None | UnsetType = UNSET,
    ) -> TestingCreateOrgUnitOrgUnitCreate:
        query = gql(
            """
            mutation _Testing_CreateOrgUnit($name: String!, $parent: UUID, $org_unit_type: UUID!, $org_unit_level: UUID) {
              org_unit_create(
                input: {name: $name, parent: $parent, org_unit_type: $org_unit_type, org_unit_level: $org_unit_level, validity: {from: "2010-02-03"}}
              ) {
                uuid
                current {
                  org_unit_level_uuid
                }
              }
            }
            """
        )
        variables: dict[str, object] = {
            "name": name,
            "parent": parent,
            "org_unit_type": org_unit_type,
            "org_unit_level": org_unit_level,
        }
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return TestingCreateOrgUnit.parse_obj(data).org_unit_create

    async def _testing__create_employee(
        self, first_name: str, last_name: str
    ) -> TestingCreateEmployeeEmployeeCreate:
        query = gql(
            """
            mutation _Testing_CreateEmployee($first_name: String!, $last_name: String!) {
              employee_create(input: {given_name: $first_name, surname: $last_name}) {
                uuid
              }
            }
            """
        )
        variables: dict[str, object] = {
            "first_name": first_name,
            "last_name": last_name,
        }
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return TestingCreateEmployee.parse_obj(data).employee_create

    async def _testing__create_association(
        self, org_unit: UUID, person: UUID, association_type: UUID
    ) -> TestingCreateAssociationAssociationCreate:
        query = gql(
            """
            mutation _Testing_CreateAssociation($org_unit: UUID!, $person: UUID!, $association_type: UUID!) {
              association_create(
                input: {validity: {from: "2010-02-03"}, org_unit: $org_unit, association_type: $association_type, person: $person}
              ) {
                uuid
              }
            }
            """
        )
        variables: dict[str, object] = {
            "org_unit": org_unit,
            "person": person,
            "association_type": association_type,
        }
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return TestingCreateAssociation.parse_obj(data).association_create

    async def _testing__create_engagement(
        self, orgunit: UUID, person: UUID, engagement_type: UUID, job_function: UUID
    ) -> TestingCreateEngagementEngagementCreate:
        query = gql(
            """
            mutation _Testing_CreateEngagement($orgunit: UUID!, $person: UUID!, $engagement_type: UUID!, $job_function: UUID!) {
              engagement_create(
                input: {org_unit: $orgunit, engagement_type: $engagement_type, job_function: $job_function, person: $person, validity: {from: "2016-05-05"}}
              ) {
                uuid
              }
            }
            """
        )
        variables: dict[str, object] = {
            "orgunit": orgunit,
            "person": person,
            "engagement_type": engagement_type,
            "job_function": job_function,
        }
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return TestingCreateEngagement.parse_obj(data).engagement_create
