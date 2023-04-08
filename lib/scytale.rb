# frozen_string_literal: true

# Scytale Cipher
class Scytale
  def encrypt(msg, key)
    l = (msg.size / key.to_f).ceil
    msg.ljust(l * key, '*').chars.each_slice(l).to_a.transpose.join
  end

  def decrypt(msg, key)
    "#{msg} #{key}"
  end

  def long(msg_size, key)
    (msg_size / key.to_f).ceil
  end
end

# a = Scytale.encrypt('Hello World', 3, )
cipher = Scytale.new
sent = ['Vehicle plan mystery hit solution.',
        'Adapted valley late practical.',
        'Fierce remove modern independent under remain.',
        'Certainly few grew developed farther earliest help.',
        'Entirely arrange longer especially shine.',
        'Future smoke harder.',
        'Symbol star age besides.',
        'when does telling the truth ever help anybody?']

sent.each do |n|
  e_msg, msg = cipher.encrypt(n, 3)
  p msg, e_msg, msg.size, cipher.long(n.size, 3) * 3
end
