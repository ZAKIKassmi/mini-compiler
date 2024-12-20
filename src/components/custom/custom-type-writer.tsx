import React from 'react'
import { TypewriterEffectSmooth } from '../ui/typewriter-effect';

type Props = {}

export default function CustomTypeWriter({}: Props) {
  const words = [
    {
      text: "Welcom,",
    },
    {
      text: "to",
    },
    {
      text: "Poetria.",
    },
    
  ];
  return (
    <TypewriterEffectSmooth words={words}/>
  )
}