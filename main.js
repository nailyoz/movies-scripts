const fs = require('fs');

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

function extractCharacterNames(line) {
  const colonIndex = line.indexOf(':');
  if (colonIndex !== -1) {
    const characterNames = line.substring(0, colonIndex).trim().split(', ');
    return characterNames;
  }
  return [];
}

// Read the contents of the .txt file
const inputFile = 'Spiderman Script.txt'; // Replace with your input file name
const outputFile = 'output.txt'; // Replace with your output file name

fs.readFile(inputFile, 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading file:', err);
    return;
  }

  // Process the file contents
  const sections = breakTextIntoSections(data);

  // Extract and collect the character names
  const characterSets = [];
  for (const section of sections) {
    const lines = section.split('\n');
    const characterNames = [];
    for (const line of lines) {
      const names = extractCharacterNames(line);
      if (names.length > 0) {
        characterNames.push(names);
      }
    }
    characterSets.push(characterNames);
  }

  // Generate combinations of two characters for each scene
  const outputLines = [];
  for (const characters of characterSets) {
    if (characters.length >= 2) {
      for (let i = 0; i < characters.length; i++) {
        for (let j = i + 1; j < characters.length; j++) {
          const combination = `${characters[i]}, ${characters[j]}`;
          outputLines.push(combination);
        }
      }
    }
  }

  // Prepare the output text
  const outputText = outputLines.join('\n');

  // Write the output text to a new file
  fs.writeFile(outputFile, outputText, 'utf8', (err) => {
    if (err) {
      console.error('Error writing file:', err);
      return;
    }
    console.log(`Output file "${outputFile}" has been created successfully.`);
  });
});
