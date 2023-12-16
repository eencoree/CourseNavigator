SELECT course.*
FROM course
JOIN expert_course ON course.id_course = expert_course.course_id
JOIN user ON expert_course.expert_id = user.id_user
WHERE user.nickname = 'ИМЯ ЭКСПЕРТА';
