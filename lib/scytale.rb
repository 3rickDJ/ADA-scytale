# frozen_string_literal: true

# Scytale Cipher
class Scytale
  def self.encrypt(msg, key, _long)
    matrix = [[]] * key
    msg.chars.each_with_index do |char, index|
      matrix[index % key] << char
    end
    matrix.join
  end

  def decrypt(msg, key)
    "#{msg} #{key}"
  end

  def self.long(msg_size, key)
    (msg_size / key.to_f).ceil
  end
end

# a = Scytale.encrypt('Hello World', 3, )
puts Scytale.long(10, 3.0)
