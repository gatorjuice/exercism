class School
  def initialize
    @student_body = Hash.new { |hash, key| hash[key] = [] }
  end

  def students(grade)
    @student_body[grade].sort
  end

  def add(name, grade)
    @student_body[grade] << name
  end

  def students_by_grade
    @student_body.map do |grade, students|
      { grade: grade, students: students.sort }
    end.sort_by { |k, v| k[:grade] }
  end
end

module BookKeeping
  VERSION = 3
end
