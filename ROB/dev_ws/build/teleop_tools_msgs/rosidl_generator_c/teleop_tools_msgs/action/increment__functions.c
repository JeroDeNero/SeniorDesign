// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from teleop_tools_msgs:action/Increment.idl
// generated code does not contain a copyright notice
#include "teleop_tools_msgs/action/increment__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `increment_by`
#include "rosidl_generator_c/primitives_sequence_functions.h"

bool
teleop_tools_msgs__action__Increment_Goal__init(teleop_tools_msgs__action__Increment_Goal * msg)
{
  if (!msg) {
    return false;
  }
  // increment_by
  if (!rosidl_generator_c__float__Sequence__init(&msg->increment_by, 0)) {
    teleop_tools_msgs__action__Increment_Goal__fini(msg);
    return false;
  }
  return true;
}

void
teleop_tools_msgs__action__Increment_Goal__fini(teleop_tools_msgs__action__Increment_Goal * msg)
{
  if (!msg) {
    return;
  }
  // increment_by
  rosidl_generator_c__float__Sequence__fini(&msg->increment_by);
}

teleop_tools_msgs__action__Increment_Goal *
teleop_tools_msgs__action__Increment_Goal__create()
{
  teleop_tools_msgs__action__Increment_Goal * msg = (teleop_tools_msgs__action__Increment_Goal *)malloc(sizeof(teleop_tools_msgs__action__Increment_Goal));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(teleop_tools_msgs__action__Increment_Goal));
  bool success = teleop_tools_msgs__action__Increment_Goal__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
teleop_tools_msgs__action__Increment_Goal__destroy(teleop_tools_msgs__action__Increment_Goal * msg)
{
  if (msg) {
    teleop_tools_msgs__action__Increment_Goal__fini(msg);
  }
  free(msg);
}


bool
teleop_tools_msgs__action__Increment_Goal__Sequence__init(teleop_tools_msgs__action__Increment_Goal__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  teleop_tools_msgs__action__Increment_Goal * data = NULL;
  if (size) {
    data = (teleop_tools_msgs__action__Increment_Goal *)calloc(size, sizeof(teleop_tools_msgs__action__Increment_Goal));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = teleop_tools_msgs__action__Increment_Goal__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        teleop_tools_msgs__action__Increment_Goal__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
teleop_tools_msgs__action__Increment_Goal__Sequence__fini(teleop_tools_msgs__action__Increment_Goal__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      teleop_tools_msgs__action__Increment_Goal__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

teleop_tools_msgs__action__Increment_Goal__Sequence *
teleop_tools_msgs__action__Increment_Goal__Sequence__create(size_t size)
{
  teleop_tools_msgs__action__Increment_Goal__Sequence * array = (teleop_tools_msgs__action__Increment_Goal__Sequence *)malloc(sizeof(teleop_tools_msgs__action__Increment_Goal__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = teleop_tools_msgs__action__Increment_Goal__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
teleop_tools_msgs__action__Increment_Goal__Sequence__destroy(teleop_tools_msgs__action__Increment_Goal__Sequence * array)
{
  if (array) {
    teleop_tools_msgs__action__Increment_Goal__Sequence__fini(array);
  }
  free(array);
}


bool
teleop_tools_msgs__action__Increment_Result__init(teleop_tools_msgs__action__Increment_Result * msg)
{
  if (!msg) {
    return false;
  }
  // structure_needs_at_least_one_member
  return true;
}

void
teleop_tools_msgs__action__Increment_Result__fini(teleop_tools_msgs__action__Increment_Result * msg)
{
  if (!msg) {
    return;
  }
  // structure_needs_at_least_one_member
}

teleop_tools_msgs__action__Increment_Result *
teleop_tools_msgs__action__Increment_Result__create()
{
  teleop_tools_msgs__action__Increment_Result * msg = (teleop_tools_msgs__action__Increment_Result *)malloc(sizeof(teleop_tools_msgs__action__Increment_Result));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(teleop_tools_msgs__action__Increment_Result));
  bool success = teleop_tools_msgs__action__Increment_Result__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
teleop_tools_msgs__action__Increment_Result__destroy(teleop_tools_msgs__action__Increment_Result * msg)
{
  if (msg) {
    teleop_tools_msgs__action__Increment_Result__fini(msg);
  }
  free(msg);
}


bool
teleop_tools_msgs__action__Increment_Result__Sequence__init(teleop_tools_msgs__action__Increment_Result__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  teleop_tools_msgs__action__Increment_Result * data = NULL;
  if (size) {
    data = (teleop_tools_msgs__action__Increment_Result *)calloc(size, sizeof(teleop_tools_msgs__action__Increment_Result));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = teleop_tools_msgs__action__Increment_Result__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        teleop_tools_msgs__action__Increment_Result__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
teleop_tools_msgs__action__Increment_Result__Sequence__fini(teleop_tools_msgs__action__Increment_Result__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      teleop_tools_msgs__action__Increment_Result__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

teleop_tools_msgs__action__Increment_Result__Sequence *
teleop_tools_msgs__action__Increment_Result__Sequence__create(size_t size)
{
  teleop_tools_msgs__action__Increment_Result__Sequence * array = (teleop_tools_msgs__action__Increment_Result__Sequence *)malloc(sizeof(teleop_tools_msgs__action__Increment_Result__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = teleop_tools_msgs__action__Increment_Result__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
teleop_tools_msgs__action__Increment_Result__Sequence__destroy(teleop_tools_msgs__action__Increment_Result__Sequence * array)
{
  if (array) {
    teleop_tools_msgs__action__Increment_Result__Sequence__fini(array);
  }
  free(array);
}


bool
teleop_tools_msgs__action__Increment_Feedback__init(teleop_tools_msgs__action__Increment_Feedback * msg)
{
  if (!msg) {
    return false;
  }
  // structure_needs_at_least_one_member
  return true;
}

void
teleop_tools_msgs__action__Increment_Feedback__fini(teleop_tools_msgs__action__Increment_Feedback * msg)
{
  if (!msg) {
    return;
  }
  // structure_needs_at_least_one_member
}

teleop_tools_msgs__action__Increment_Feedback *
teleop_tools_msgs__action__Increment_Feedback__create()
{
  teleop_tools_msgs__action__Increment_Feedback * msg = (teleop_tools_msgs__action__Increment_Feedback *)malloc(sizeof(teleop_tools_msgs__action__Increment_Feedback));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(teleop_tools_msgs__action__Increment_Feedback));
  bool success = teleop_tools_msgs__action__Increment_Feedback__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
teleop_tools_msgs__action__Increment_Feedback__destroy(teleop_tools_msgs__action__Increment_Feedback * msg)
{
  if (msg) {
    teleop_tools_msgs__action__Increment_Feedback__fini(msg);
  }
  free(msg);
}


bool
teleop_tools_msgs__action__Increment_Feedback__Sequence__init(teleop_tools_msgs__action__Increment_Feedback__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  teleop_tools_msgs__action__Increment_Feedback * data = NULL;
  if (size) {
    data = (teleop_tools_msgs__action__Increment_Feedback *)calloc(size, sizeof(teleop_tools_msgs__action__Increment_Feedback));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = teleop_tools_msgs__action__Increment_Feedback__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        teleop_tools_msgs__action__Increment_Feedback__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
teleop_tools_msgs__action__Increment_Feedback__Sequence__fini(teleop_tools_msgs__action__Increment_Feedback__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      teleop_tools_msgs__action__Increment_Feedback__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

teleop_tools_msgs__action__Increment_Feedback__Sequence *
teleop_tools_msgs__action__Increment_Feedback__Sequence__create(size_t size)
{
  teleop_tools_msgs__action__Increment_Feedback__Sequence * array = (teleop_tools_msgs__action__Increment_Feedback__Sequence *)malloc(sizeof(teleop_tools_msgs__action__Increment_Feedback__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = teleop_tools_msgs__action__Increment_Feedback__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
teleop_tools_msgs__action__Increment_Feedback__Sequence__destroy(teleop_tools_msgs__action__Increment_Feedback__Sequence * array)
{
  if (array) {
    teleop_tools_msgs__action__Increment_Feedback__Sequence__fini(array);
  }
  free(array);
}


// Include directives for member types
// Member `goal_id`
#include "unique_identifier_msgs/msg/uuid__functions.h"
// Member `goal`
// already included above
// #include "teleop_tools_msgs/action/increment__functions.h"

bool
teleop_tools_msgs__action__Increment_SendGoal_Request__init(teleop_tools_msgs__action__Increment_SendGoal_Request * msg)
{
  if (!msg) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__init(&msg->goal_id)) {
    teleop_tools_msgs__action__Increment_SendGoal_Request__fini(msg);
    return false;
  }
  // goal
  if (!teleop_tools_msgs__action__Increment_Goal__init(&msg->goal)) {
    teleop_tools_msgs__action__Increment_SendGoal_Request__fini(msg);
    return false;
  }
  return true;
}

void
teleop_tools_msgs__action__Increment_SendGoal_Request__fini(teleop_tools_msgs__action__Increment_SendGoal_Request * msg)
{
  if (!msg) {
    return;
  }
  // goal_id
  unique_identifier_msgs__msg__UUID__fini(&msg->goal_id);
  // goal
  teleop_tools_msgs__action__Increment_Goal__fini(&msg->goal);
}

teleop_tools_msgs__action__Increment_SendGoal_Request *
teleop_tools_msgs__action__Increment_SendGoal_Request__create()
{
  teleop_tools_msgs__action__Increment_SendGoal_Request * msg = (teleop_tools_msgs__action__Increment_SendGoal_Request *)malloc(sizeof(teleop_tools_msgs__action__Increment_SendGoal_Request));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(teleop_tools_msgs__action__Increment_SendGoal_Request));
  bool success = teleop_tools_msgs__action__Increment_SendGoal_Request__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
teleop_tools_msgs__action__Increment_SendGoal_Request__destroy(teleop_tools_msgs__action__Increment_SendGoal_Request * msg)
{
  if (msg) {
    teleop_tools_msgs__action__Increment_SendGoal_Request__fini(msg);
  }
  free(msg);
}


bool
teleop_tools_msgs__action__Increment_SendGoal_Request__Sequence__init(teleop_tools_msgs__action__Increment_SendGoal_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  teleop_tools_msgs__action__Increment_SendGoal_Request * data = NULL;
  if (size) {
    data = (teleop_tools_msgs__action__Increment_SendGoal_Request *)calloc(size, sizeof(teleop_tools_msgs__action__Increment_SendGoal_Request));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = teleop_tools_msgs__action__Increment_SendGoal_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        teleop_tools_msgs__action__Increment_SendGoal_Request__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
teleop_tools_msgs__action__Increment_SendGoal_Request__Sequence__fini(teleop_tools_msgs__action__Increment_SendGoal_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      teleop_tools_msgs__action__Increment_SendGoal_Request__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

teleop_tools_msgs__action__Increment_SendGoal_Request__Sequence *
teleop_tools_msgs__action__Increment_SendGoal_Request__Sequence__create(size_t size)
{
  teleop_tools_msgs__action__Increment_SendGoal_Request__Sequence * array = (teleop_tools_msgs__action__Increment_SendGoal_Request__Sequence *)malloc(sizeof(teleop_tools_msgs__action__Increment_SendGoal_Request__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = teleop_tools_msgs__action__Increment_SendGoal_Request__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
teleop_tools_msgs__action__Increment_SendGoal_Request__Sequence__destroy(teleop_tools_msgs__action__Increment_SendGoal_Request__Sequence * array)
{
  if (array) {
    teleop_tools_msgs__action__Increment_SendGoal_Request__Sequence__fini(array);
  }
  free(array);
}


// Include directives for member types
// Member `stamp`
#include "builtin_interfaces/msg/time__functions.h"

bool
teleop_tools_msgs__action__Increment_SendGoal_Response__init(teleop_tools_msgs__action__Increment_SendGoal_Response * msg)
{
  if (!msg) {
    return false;
  }
  // accepted
  // stamp
  if (!builtin_interfaces__msg__Time__init(&msg->stamp)) {
    teleop_tools_msgs__action__Increment_SendGoal_Response__fini(msg);
    return false;
  }
  return true;
}

void
teleop_tools_msgs__action__Increment_SendGoal_Response__fini(teleop_tools_msgs__action__Increment_SendGoal_Response * msg)
{
  if (!msg) {
    return;
  }
  // accepted
  // stamp
  builtin_interfaces__msg__Time__fini(&msg->stamp);
}

teleop_tools_msgs__action__Increment_SendGoal_Response *
teleop_tools_msgs__action__Increment_SendGoal_Response__create()
{
  teleop_tools_msgs__action__Increment_SendGoal_Response * msg = (teleop_tools_msgs__action__Increment_SendGoal_Response *)malloc(sizeof(teleop_tools_msgs__action__Increment_SendGoal_Response));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(teleop_tools_msgs__action__Increment_SendGoal_Response));
  bool success = teleop_tools_msgs__action__Increment_SendGoal_Response__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
teleop_tools_msgs__action__Increment_SendGoal_Response__destroy(teleop_tools_msgs__action__Increment_SendGoal_Response * msg)
{
  if (msg) {
    teleop_tools_msgs__action__Increment_SendGoal_Response__fini(msg);
  }
  free(msg);
}


bool
teleop_tools_msgs__action__Increment_SendGoal_Response__Sequence__init(teleop_tools_msgs__action__Increment_SendGoal_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  teleop_tools_msgs__action__Increment_SendGoal_Response * data = NULL;
  if (size) {
    data = (teleop_tools_msgs__action__Increment_SendGoal_Response *)calloc(size, sizeof(teleop_tools_msgs__action__Increment_SendGoal_Response));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = teleop_tools_msgs__action__Increment_SendGoal_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        teleop_tools_msgs__action__Increment_SendGoal_Response__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
teleop_tools_msgs__action__Increment_SendGoal_Response__Sequence__fini(teleop_tools_msgs__action__Increment_SendGoal_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      teleop_tools_msgs__action__Increment_SendGoal_Response__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

teleop_tools_msgs__action__Increment_SendGoal_Response__Sequence *
teleop_tools_msgs__action__Increment_SendGoal_Response__Sequence__create(size_t size)
{
  teleop_tools_msgs__action__Increment_SendGoal_Response__Sequence * array = (teleop_tools_msgs__action__Increment_SendGoal_Response__Sequence *)malloc(sizeof(teleop_tools_msgs__action__Increment_SendGoal_Response__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = teleop_tools_msgs__action__Increment_SendGoal_Response__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
teleop_tools_msgs__action__Increment_SendGoal_Response__Sequence__destroy(teleop_tools_msgs__action__Increment_SendGoal_Response__Sequence * array)
{
  if (array) {
    teleop_tools_msgs__action__Increment_SendGoal_Response__Sequence__fini(array);
  }
  free(array);
}


// Include directives for member types
// Member `goal_id`
// already included above
// #include "unique_identifier_msgs/msg/uuid__functions.h"

bool
teleop_tools_msgs__action__Increment_GetResult_Request__init(teleop_tools_msgs__action__Increment_GetResult_Request * msg)
{
  if (!msg) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__init(&msg->goal_id)) {
    teleop_tools_msgs__action__Increment_GetResult_Request__fini(msg);
    return false;
  }
  return true;
}

void
teleop_tools_msgs__action__Increment_GetResult_Request__fini(teleop_tools_msgs__action__Increment_GetResult_Request * msg)
{
  if (!msg) {
    return;
  }
  // goal_id
  unique_identifier_msgs__msg__UUID__fini(&msg->goal_id);
}

teleop_tools_msgs__action__Increment_GetResult_Request *
teleop_tools_msgs__action__Increment_GetResult_Request__create()
{
  teleop_tools_msgs__action__Increment_GetResult_Request * msg = (teleop_tools_msgs__action__Increment_GetResult_Request *)malloc(sizeof(teleop_tools_msgs__action__Increment_GetResult_Request));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(teleop_tools_msgs__action__Increment_GetResult_Request));
  bool success = teleop_tools_msgs__action__Increment_GetResult_Request__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
teleop_tools_msgs__action__Increment_GetResult_Request__destroy(teleop_tools_msgs__action__Increment_GetResult_Request * msg)
{
  if (msg) {
    teleop_tools_msgs__action__Increment_GetResult_Request__fini(msg);
  }
  free(msg);
}


bool
teleop_tools_msgs__action__Increment_GetResult_Request__Sequence__init(teleop_tools_msgs__action__Increment_GetResult_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  teleop_tools_msgs__action__Increment_GetResult_Request * data = NULL;
  if (size) {
    data = (teleop_tools_msgs__action__Increment_GetResult_Request *)calloc(size, sizeof(teleop_tools_msgs__action__Increment_GetResult_Request));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = teleop_tools_msgs__action__Increment_GetResult_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        teleop_tools_msgs__action__Increment_GetResult_Request__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
teleop_tools_msgs__action__Increment_GetResult_Request__Sequence__fini(teleop_tools_msgs__action__Increment_GetResult_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      teleop_tools_msgs__action__Increment_GetResult_Request__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

teleop_tools_msgs__action__Increment_GetResult_Request__Sequence *
teleop_tools_msgs__action__Increment_GetResult_Request__Sequence__create(size_t size)
{
  teleop_tools_msgs__action__Increment_GetResult_Request__Sequence * array = (teleop_tools_msgs__action__Increment_GetResult_Request__Sequence *)malloc(sizeof(teleop_tools_msgs__action__Increment_GetResult_Request__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = teleop_tools_msgs__action__Increment_GetResult_Request__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
teleop_tools_msgs__action__Increment_GetResult_Request__Sequence__destroy(teleop_tools_msgs__action__Increment_GetResult_Request__Sequence * array)
{
  if (array) {
    teleop_tools_msgs__action__Increment_GetResult_Request__Sequence__fini(array);
  }
  free(array);
}


// Include directives for member types
// Member `result`
// already included above
// #include "teleop_tools_msgs/action/increment__functions.h"

bool
teleop_tools_msgs__action__Increment_GetResult_Response__init(teleop_tools_msgs__action__Increment_GetResult_Response * msg)
{
  if (!msg) {
    return false;
  }
  // status
  // result
  if (!teleop_tools_msgs__action__Increment_Result__init(&msg->result)) {
    teleop_tools_msgs__action__Increment_GetResult_Response__fini(msg);
    return false;
  }
  return true;
}

void
teleop_tools_msgs__action__Increment_GetResult_Response__fini(teleop_tools_msgs__action__Increment_GetResult_Response * msg)
{
  if (!msg) {
    return;
  }
  // status
  // result
  teleop_tools_msgs__action__Increment_Result__fini(&msg->result);
}

teleop_tools_msgs__action__Increment_GetResult_Response *
teleop_tools_msgs__action__Increment_GetResult_Response__create()
{
  teleop_tools_msgs__action__Increment_GetResult_Response * msg = (teleop_tools_msgs__action__Increment_GetResult_Response *)malloc(sizeof(teleop_tools_msgs__action__Increment_GetResult_Response));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(teleop_tools_msgs__action__Increment_GetResult_Response));
  bool success = teleop_tools_msgs__action__Increment_GetResult_Response__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
teleop_tools_msgs__action__Increment_GetResult_Response__destroy(teleop_tools_msgs__action__Increment_GetResult_Response * msg)
{
  if (msg) {
    teleop_tools_msgs__action__Increment_GetResult_Response__fini(msg);
  }
  free(msg);
}


bool
teleop_tools_msgs__action__Increment_GetResult_Response__Sequence__init(teleop_tools_msgs__action__Increment_GetResult_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  teleop_tools_msgs__action__Increment_GetResult_Response * data = NULL;
  if (size) {
    data = (teleop_tools_msgs__action__Increment_GetResult_Response *)calloc(size, sizeof(teleop_tools_msgs__action__Increment_GetResult_Response));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = teleop_tools_msgs__action__Increment_GetResult_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        teleop_tools_msgs__action__Increment_GetResult_Response__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
teleop_tools_msgs__action__Increment_GetResult_Response__Sequence__fini(teleop_tools_msgs__action__Increment_GetResult_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      teleop_tools_msgs__action__Increment_GetResult_Response__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

teleop_tools_msgs__action__Increment_GetResult_Response__Sequence *
teleop_tools_msgs__action__Increment_GetResult_Response__Sequence__create(size_t size)
{
  teleop_tools_msgs__action__Increment_GetResult_Response__Sequence * array = (teleop_tools_msgs__action__Increment_GetResult_Response__Sequence *)malloc(sizeof(teleop_tools_msgs__action__Increment_GetResult_Response__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = teleop_tools_msgs__action__Increment_GetResult_Response__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
teleop_tools_msgs__action__Increment_GetResult_Response__Sequence__destroy(teleop_tools_msgs__action__Increment_GetResult_Response__Sequence * array)
{
  if (array) {
    teleop_tools_msgs__action__Increment_GetResult_Response__Sequence__fini(array);
  }
  free(array);
}


// Include directives for member types
// Member `goal_id`
// already included above
// #include "unique_identifier_msgs/msg/uuid__functions.h"
// Member `feedback`
// already included above
// #include "teleop_tools_msgs/action/increment__functions.h"

bool
teleop_tools_msgs__action__Increment_FeedbackMessage__init(teleop_tools_msgs__action__Increment_FeedbackMessage * msg)
{
  if (!msg) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__init(&msg->goal_id)) {
    teleop_tools_msgs__action__Increment_FeedbackMessage__fini(msg);
    return false;
  }
  // feedback
  if (!teleop_tools_msgs__action__Increment_Feedback__init(&msg->feedback)) {
    teleop_tools_msgs__action__Increment_FeedbackMessage__fini(msg);
    return false;
  }
  return true;
}

void
teleop_tools_msgs__action__Increment_FeedbackMessage__fini(teleop_tools_msgs__action__Increment_FeedbackMessage * msg)
{
  if (!msg) {
    return;
  }
  // goal_id
  unique_identifier_msgs__msg__UUID__fini(&msg->goal_id);
  // feedback
  teleop_tools_msgs__action__Increment_Feedback__fini(&msg->feedback);
}

teleop_tools_msgs__action__Increment_FeedbackMessage *
teleop_tools_msgs__action__Increment_FeedbackMessage__create()
{
  teleop_tools_msgs__action__Increment_FeedbackMessage * msg = (teleop_tools_msgs__action__Increment_FeedbackMessage *)malloc(sizeof(teleop_tools_msgs__action__Increment_FeedbackMessage));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(teleop_tools_msgs__action__Increment_FeedbackMessage));
  bool success = teleop_tools_msgs__action__Increment_FeedbackMessage__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
teleop_tools_msgs__action__Increment_FeedbackMessage__destroy(teleop_tools_msgs__action__Increment_FeedbackMessage * msg)
{
  if (msg) {
    teleop_tools_msgs__action__Increment_FeedbackMessage__fini(msg);
  }
  free(msg);
}


bool
teleop_tools_msgs__action__Increment_FeedbackMessage__Sequence__init(teleop_tools_msgs__action__Increment_FeedbackMessage__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  teleop_tools_msgs__action__Increment_FeedbackMessage * data = NULL;
  if (size) {
    data = (teleop_tools_msgs__action__Increment_FeedbackMessage *)calloc(size, sizeof(teleop_tools_msgs__action__Increment_FeedbackMessage));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = teleop_tools_msgs__action__Increment_FeedbackMessage__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        teleop_tools_msgs__action__Increment_FeedbackMessage__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
teleop_tools_msgs__action__Increment_FeedbackMessage__Sequence__fini(teleop_tools_msgs__action__Increment_FeedbackMessage__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      teleop_tools_msgs__action__Increment_FeedbackMessage__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

teleop_tools_msgs__action__Increment_FeedbackMessage__Sequence *
teleop_tools_msgs__action__Increment_FeedbackMessage__Sequence__create(size_t size)
{
  teleop_tools_msgs__action__Increment_FeedbackMessage__Sequence * array = (teleop_tools_msgs__action__Increment_FeedbackMessage__Sequence *)malloc(sizeof(teleop_tools_msgs__action__Increment_FeedbackMessage__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = teleop_tools_msgs__action__Increment_FeedbackMessage__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
teleop_tools_msgs__action__Increment_FeedbackMessage__Sequence__destroy(teleop_tools_msgs__action__Increment_FeedbackMessage__Sequence * array)
{
  if (array) {
    teleop_tools_msgs__action__Increment_FeedbackMessage__Sequence__fini(array);
  }
  free(array);
}
