SELECT user.*
FROM user
JOIN student_course ON user.id_user = student_course.student_id
JOIN content ON student_course.course_id = content.id_course
JOIN step_student ON content.step_id = step_student.step_id
WHERE content.title = "название курса"
  AND step_student.status = 'done'
GROUP BY user.id_user
HAVING COUNT(DISTINCT step_student.step_id) = (SELECT COUNT(*) FROM step WHERE task_id IS NOT NULL);
