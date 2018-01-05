module BookKeeping
  VERSION = 1 # Where the version number matches the one in the test.
end

class Bob
  def self.hey(remark)
    remark.strip!
    punctuation = (remark[-1] if remark.end_with?('?', '!', '.')) || ''
    stripped_remark = (remark.scan(/[a-zA-Z]+/).join()) || ''

    if remark.empty?
      'Fine. Be that way!'
    elsif !stripped_remark.empty? && remark.upcase == remark
      'Whoa, chill out!'
    elsif punctuation == '?'
      'Sure.'
    else
      'Whatever.'
    end
  end
end
