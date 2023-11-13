from greenfield_python_sdk.models.eip712_messages.group import (
    msg_create_group,
    msg_delete_group,
    msg_leave_group,
    msg_renew_group_member,
    msg_update_group_member,
)
from greenfield_python_sdk.models.eip712_messages.group.group_url import (
    CREATE_GROUP,
    DELETE_GROUP,
    LEAVE_GROUP,
    RENEW_GROUP_MEMEBER,
    UPDATE_GROUP_MEMBER,
)

TYPES_MAP = {
    CREATE_GROUP: msg_create_group.TYPES,
    DELETE_GROUP: msg_delete_group.TYPES,
    UPDATE_GROUP_MEMBER: msg_update_group_member.TYPES,
    LEAVE_GROUP: msg_leave_group.TYPES,
    RENEW_GROUP_MEMEBER: msg_renew_group_member.TYPES,
}
