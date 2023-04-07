# frozen_string_literal: true

# Scytale Cipher
class Scytale

  def encrypt(msg, key)
    "#{msg} #{key}"
  end

  def decrypt(msg, key)
    "#{msg} #{key}"
  end

  private
end

a = Scytale.encrypt('Hello World', 3)
puts a
