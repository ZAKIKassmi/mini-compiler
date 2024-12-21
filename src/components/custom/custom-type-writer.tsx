import React from 'react'
import { TypewriterEffectSmooth } from '../ui/typewriter-effect';

type Props = {}

export default function CustomTypeWriter({}: Props) {
  const words = [
    {
      text: "Welcome,",
    },
    {
      text: "to",
    },
    {
      text: "Poetria.",
      className: "text-red-500 dark:text-red-500",
    },
    
  ];
  return (
    <TypewriterEffectSmooth words={words}/>
  )
}