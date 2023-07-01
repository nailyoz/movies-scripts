function breakTextIntoSections(text) {
    const sections = [];
    const pattern = /\[(.*?)\]/g;
    let match;
    let lastIndex = 0;
  
    while ((match = pattern.exec(text)) !== null) {
      const sectionStartIndex = match.index + match[0].length;
      const sectionEndIndex = pattern.lastIndex;
      const section = text.substring(sectionStartIndex, sectionEndIndex).trim();
      sections.push(section);
      lastIndex = pattern.lastIndex;
    }
  
    // Add the remaining text after the last section
    if (lastIndex < text.length) {
      const remainingText = text.substring(lastIndex).trim();
      if (remainingText.length > 0) {
        sections.push(remainingText);
      }
    }
  
    return sections;
  }
  
  function extractCharacterName(line) {
    const colonIndex = line.indexOf(':');
    if (colonIndex !== -1) {
      const characterName = line.substring(0, colonIndex).trim();
      return characterName;
    }
    return '';
  }
  
  // Example usage
  const text = `[OVER COLUMBIA LOGO:]
  Quentin Beck [vo]: I managed to send the Elemental back through the dimensional rift, but I don't think I'm gonna make it off this bridge alive. Spider-Man attacked me for some reason! He has an army of weaponized drones, Stark technology. He's saying he's the only one who's gonna be the new Iron Man, no one else!
  E.D.I.T.H. [vo]: Are you sure you want to commence the drone attack? There will be significant casualties.
  Peter Parker [vo]: Do it! Execute them all!
  [DRONES FIRE! EXPLOSIONS from the Tower Bridge.]
  [OVER MARVEL LOGO:]
  Pat Kiernan [vo]: This shocking video was released earlier today, on the controversial news website TheDailyBugle.net.`;
  
  const sections = breakTextIntoSections(text);
  for (const section of sections) {
    const lines = section.split('\n');
    for (const line of lines) {
      const characterName = extractCharacterName(line);
      console.log('Input:', characterName);
      console.log('Output:', line);
      console.log('---');
    }
  }
  