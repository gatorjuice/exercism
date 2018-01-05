module.exports = class School {
  constructor() {
    this.studentBody = {}
  }

  roster() {
    return this.studentBody;
  }

  add(name, grade) {
    if (!this.studentBody[grade]) {
      this.studentBody[grade] = [];
    }
    this.studentBody[grade].push(name)
    this.studentBody[grade].sort();
  }

  grade(number) {
    return this.studentBody[number] || []
  }
}
