SELECT task.title, status.status_type
FROM task
JOIN step_student ON task.id_task = step_student.step_id
JOIN status ON step_student.status_id = status.id_status
WHERE step_student.user_id = 1 AND step_student.status_id = “done”;
