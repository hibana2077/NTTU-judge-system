<!--
 * @Author: hibana2077 hibana2077@gmaill.com
 * @Date: 2023-10-17 11:11:43
 * @LastEditors: hibana2077 hibana2077@gmaill.com
 * @LastEditTime: 2023-10-17 11:18:27
 * @FilePath: /NTTU-new-gen-judge-system/backend/schema.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# schema

1. **用戶（Users）**
2. **題目（Problems）**
3. **提交（Submissions）**
4. **比賽（Contests）**

## 詳細資料

### 用戶（Users）

```json
{
    "_id": ObjectId,
    "username": String,
    "password": String, // 加密過的密碼
    "email": String,
    "roles": [String],  // ["admin", "user", "judge"]
    "created_at": Date,
    "last_login": Date
}
```

### 題目（Problems）

```json
{
    "_id": ObjectId,
    "title": String,
    "description": String,
    "input_format": String,
    "output_format": String,
    "sample_input": String,
    "sample_output": String,
    "time_limit": Number, // 毫秒
    "memory_limit": Number, // MB
    "tags": [String], // ["Array", "Math", "DP"]
    "created_by": ObjectId, // User 的 _id
    "created_at": Date
}
```

### 提交（Submissions）

```json
{
    "_id": ObjectId,
    "user_id": ObjectId, // User 的 _id
    "problem_id": ObjectId, // Problem 的 _id
    "code": String, // 提交的代碼
    "language": String, // ["C++", "Python", "Java"]
    "status": String, // ["Accepted", "Wrong Answer", "Time Limit Exceeded"]
    "time_used": Number, // 毫秒
    "memory_used": Number, // MB
    "submitted_at": Date
}
```

### 比賽（Contests）

```json
{
    "_id": ObjectId,
    "title": String,
    "description": String,
    "start_time": Date,
    "end_time": Date,
    "problems": [ObjectId], // Problem 的 _id 列表
    "participants": [ObjectId], // User 的 _id 列表
    "created_by": ObjectId, // User 的 _id
    "created_at": Date
}
```

### 公告 (Announcements)

```json
{
    "_id": ObjectId,
    "title": String,
    "content": String,
    "created_by": ObjectId, // User 的 _id
    "created_at": Date
}
```