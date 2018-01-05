class Game
  def initialize
    @turn = 0
    @frame = 0
    @frames = [
      [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
      [0, 0], [0, 0], [0, 0], [0, 0], [0, 0, 0]
    ]
  end

  def roll(pins)
    if pins == 10
      @turn = 0
      @frames[@frame + 1][0] += 10
      @frames[@frame + 1][0] += 10
      @frame += 1
    else
      if @turn == 0
        @frames[@frame][0] += pins
        @turn += 1
      elsif @turn == 1 && @frames[@frame][0] + pins == 10
        @frames[@frame + 1][0] += pins * 2
        @turn = 0
      else
        @frames[@frame][1] += pins
        @turn = 0
      end
    end
  end

  #   else
  #   end
  #   if @top
  #     if pins == 10
  #       @frames[@frame + 1][0] += 10
  #       @frames[@frame + 1][1] += 10
  #       @top = true
  #       @frame += 1
  #     else
  #       @frames[@frame][0] += pins
  #       @top = false
  #     end
  #   elsif @frame <= 9
  #     if @frames[@frame][0] + pins == 10
  #       @frames[@frame + 1][0] += 10
  #     else
  #       p @frames[@frame]
  #       @frames[@frame][1] += pins
  #     end
  #     @top = true
  #     @frame += 1
  #   else
  #     p 'got here'
  #   end
  # end

  def score
    @frames.flatten.reduce(:+)
  end
end
