SELECT DISTINCT u.id_user, u.nickname
FROM user u
JOIN step_student ss ON u.id_user = ss.user_id
JOIN content c ON ss.step_id = c.step_id
JOIN course crs ON c.course_id = crs.id_course
JOIN status s ON ss.status_id = s.id_status
WHERE crs.id_course = 1 AND s.status_type = 'done'
GROUP BY u.id_user, u.nickname
HAVING COUNT(DISTINCT c.id_content) = (SELECT COUNT(DISTINCT id_step) FROM step WHERE task_id IS NOT NULL AND step.course_id = crs.id_course);
