# frozen_string_literal: true

# Scytale Cipher
class Scytale
  def encrypt(msg, key)
    l = (msg.size / key.to_f).ceil
    msg.ljust(l * key, '*').chars.each_slice(l).to_a.transpose.join
  end

  def decrypt(msg, key)
    msg.chars.each_slice(key).to_a.transpose.join
  end
end

if $0 == __FILE__
  cipher = Scytale.new
  sent = ['Vehicle plan mystery hit solution.',
          'Adapted valley late practical.',
          'Fierce remove modern independent under remain.',
          'Certainly few grew developed farther earliest help.',
          'Entirely arrange longer especially shine.',
          'Future smoke harder.',
          'Symbol star age besides.',
          'when does telling the truth ever help anybody?',
          <<~TXT
            Este es un ejemplo de texto para cifrar con el algoritmo Escítala.
            Podemos cifrar cualquier texto que queramos, siempre y cuando
            especifiquemos el número de líneas a utilizar en el cifrado.
          TXT
  ]

  sent.each do |n|
    key = rand(2..(n.size / 2))
    e_msg = cipher.encrypt(n, key)
    d_msg = cipher.decrypt(e_msg, key)
    puts <<~TXT
      it '#{d_msg}' do
        e_msg = '#{e_msg}'
        key = #{key}
        d_msg = '#{d_msg}'
        expect(cipher.decrypt(e_msg, key)).to eq(d_msg)
      end
    TXT
  end
end
