require 'scytale'

describe Scytale do
  let(:cipher) { Scytale.new }
  describe 'encrypt a message' do
    it 'returns the encrypted message' do
      msg = 'Vehicle plan mystery hit solution.'
      key = 7
      e_msg = 'Vlas sieenthooh  eilnipmrtu.clyy t*'
      expect(cipher.encrypt(msg, key)).to eq(e_msg)
    end
    it 'returns Apdaelerta****dt lya ail****aevl tpcc.****' do
      msg = 'Adapted valley late practical.'
      key = 14
      e_msg = 'Apdaelerta****dt lya ail****aevl tpcc.****'
      expect(cipher.encrypt(msg, key)).to eq(e_msg)
    end
    it 'returns F ereneair nptrieem e  nrmoinur.codndne*evededm*' do
      msg = 'Fierce remove modern independent under remain.'
      key = 8
      e_msg = 'F ereneair nptrieem e  nrmoinur.codndne*evededm*'
      expect(cipher.encrypt(msg, key)).to eq(e_msg)
    end
    it 'returns Cnw oa elel dpresprygeetat.t rvdhr *afee elh*iewlfrie*' do
      msg = 'Certainly few grew developed farther earliest help.'
      key = 9
      e_msg = 'Cnw oa elel dpresprygeetat.t rvdhr *afee elh*iewlfrie*'
      expect(cipher.encrypt(msg, key)).to eq(e_msg)
    end
    it 'returns Eygecsn erihta  aiirlelnrrosleeanpy.lnge *' do
      msg = 'Entirely arrange longer especially shine.'
      key = 6
      e_msg = 'Eygecsn erihta  aiirlelnrrosleeanpy.lnge *'
      expect(cipher.encrypt(msg, key)).to eq(e_msg)
    end
    it 'returns Fu o rr**urskhd.**temeae***' do
      msg = 'Future smoke harder.'
      key = 9
      e_msg = 'Fu o rr**urskhd.**temeae***'
      expect(cipher.encrypt(msg, key)).to eq(e_msg)
    end
    it 'returns Slr dy  bemsaesbtgs.oaei*' do
      msg = 'Symbol star age besides.'
      key = 5
      e_msg = 'Slr dy  bemsaesbtgs.oaei*'
      expect(cipher.encrypt(msg, key)).to eq(e_msg)
    end
    it 'returns w slgeue pyy**hd l  tvh b?**eotittheeao***neenhr rlnd***' do
      msg = 'when does telling the truth ever help anybody?'
      key = 14
      e_msg = 'w slgeue pyy**hd l  tvh b?**eotittheeao***neenhr rlnd***'
      expect(cipher.encrypt(msg, key)).to eq(e_msg)
    end
  end
  describe 'decrypt a message' do
    it 'Vehicle plan mystery hit solution.**********' do
      e_msg = 'Vcp t  un**ellmehst.**heayrioi***i nsytlo***'
      key = 11
      d_msg = 'Vehicle plan mystery hit solution.**********'
      expect(cipher.decrypt(e_msg, key)).to eq(d_msg)
    end
    it 'Adapted valley late practical.' do
      e_msg = 'Adeetd y iav pcpalratlaaleltc.'
      key = 5
      d_msg = 'Adapted valley late practical.'
      expect(cipher.decrypt(e_msg, key)).to eq(d_msg)
    end
    it 'Fierce remove modern independent under remain.*********' do
      e_msg = 'Feoo pnde.*i vdietem**ereenn ra**re rddu i**cmmneenrn**'
      key = 11
      d_msg = 'Fierce remove modern independent under remain.*********'
      expect(cipher.decrypt(e_msg, key)).to eq(d_msg)
    end
    it 'Certainly few grew developed farther earliest help.*********' do
      e_msg = 'Cifreparl .*eneever ih**rlwwedteee**ty  l hasl**a gdofertp**'
      key = 12
      d_msg = 'Certainly few grew developed farther earliest help.*********'
      expect(cipher.decrypt(e_msg, key)).to eq(d_msg)
    end
    it 'Entirely arrange longer especially shine.***********' do
      e_msg = 'Er a geclh.**neanlesiyi***tlrgorpa n***iyren else***'
      key = 13
      d_msg = 'Entirely arrange longer especially shine.***********'
      expect(cipher.decrypt(e_msg, key)).to eq(d_msg)
    end
    it 'Future smoke harder.*' do
      e_msg = 'Fsaumrtodukerere . h*'
      key = 3
      d_msg = 'Future smoke harder.*'
      expect(cipher.decrypt(e_msg, key)).to eq(d_msg)
    end
    it 'Symbol star age besides.' do
      e_msg = 'Stbyaemrsb ioadlge ess .'
      key = 3
      d_msg = 'Symbol star age besides.'
      expect(cipher.decrypt(e_msg, key)).to eq(d_msg)
    end
    it 'when does telling the truth ever help anybody?**' do
      e_msg = 'wluphlt eihann n geyd vboteoehrdse y  h?tte*erl*'
      key = 4
      d_msg = 'when does telling the truth ever help anybody?**'
      expect(cipher.decrypt(e_msg, key)).to eq(d_msg)
    end
  end
end
