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
from rbac.common.task.propose_admin import ProposeAddTaskAdmin
from rbac.common.task.confirm_admin import ConfirmAddTaskAdmin
from rbac.common.task.reject_admin import RejectAddTaskAdmin

LOGGER = logging.getLogger(__name__)


class AdminRelationship(BaseRelationship):
    def __init__(self):
        BaseRelationship.__init__(self)
        self.propose = ProposeAddTaskAdmin()
        self.confirm = ConfirmAddTaskAdmin()
        self.reject = RejectAddTaskAdmin()

    @property
    def name(self):
        return "task"

    @property
    def container_proto(self):
        return protobuf.task_state_pb2.TaskRelationshipContainer

    def address(self, object_id, target_id):
        return addresser.task.admin.address(object_id, target_id)
