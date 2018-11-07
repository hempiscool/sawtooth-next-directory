# Copyright 2018 Contributors to Hyperledger Sawtooth
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -----------------------------------------------------------------------------

import logging

from rbac.common import addresser
from rbac.common import protobuf
from rbac.common.base.base_relationship import BaseRelationship
from rbac.common.role.propose_member import ProposeAddRoleMember
from rbac.common.role.confirm_member import ConfirmAddRoleMember
from rbac.common.role.reject_member import RejectAddRoleMember

LOGGER = logging.getLogger(__name__)


class MemberRelationship(BaseRelationship):
    def __init__(self):
        BaseRelationship.__init__(self)
        self.propose = ProposeAddRoleMember()
        self.confirm = ConfirmAddRoleMember()
        self.reject = RejectAddRoleMember()

    @property
    def name(self):
        return "role"

    @property
    def container_proto(self):
        return protobuf.role_state_pb2.RoleRelationshipContainer

    def address(self, object_id, target_id):
        return addresser.role.member.address(object_id, target_id)
