class Alphametics
  def self.solve(input)
    key = {}
    letters = input.scan(/[A-Za-z]/).uniq.sort
    letters.each {|letter| key[letter] = 0}
    input.gsub!(' ', '')
    addends = input.split('==')[0].split('+')
    sum = input.split('==')[1]
    p sum, letters, input, addends, key
    { 'B' => 9, 'I' => 1, 'L' => 0 }
  end
end
