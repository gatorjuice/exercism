class Triangle
  def initialize(sides)
    @sides = sides
  end

  def equilateral?
    @sides.uniq.length == 1 unless sides_invalid?
  end

  def isosceles?
    @sides.uniq.length <= 2 unless sides_invalid?
  end

  def scalene?
    @sides.uniq.length == 3 unless sides_invalid?
  end

  private

  def sides_invalid?
    @sides.include?(0) || @sides.permutation(3).any? do |perm|
      perm.first(2).sum < perm.last
    end
  end
end

module BookKeeping
  VERSION = 1
end
