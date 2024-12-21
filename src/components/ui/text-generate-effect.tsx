"use client";
import { useEffect } from "react";
import { motion, stagger, useAnimate } from "framer-motion";
import { cn } from "@/lib/utils";

export const TextGenerateEffect = ({
  words,
  className,
  filter = true,
  duration = 0.5,
}: {
  words: string;
  className?: string;
  filter?: boolean;
  duration?: number;
}) => {
  const [scope, animate] = useAnimate();
  
  // Split by newlines first, then split each line by spaces
  const lines = words.split("\n");
  const wordsWithLineBreaks = lines.flatMap((line, lineIndex) => {
    const lineWords = line.split(" ").filter(word => word.length > 0);
    return lineIndex < lines.length - 1 
      ? [...lineWords, "\n"] 
      : lineWords;
  });

  useEffect(() => {
    animate(
      "span",
      {
        opacity: 1,
        filter: filter ? "blur(0px)" : "none",
      },
      {
        duration: duration ? duration : 1,
        delay: stagger(0.2),
      }
    );
  }, [scope.current, animate, duration, filter]);

  useEffect(() => {
    renderWords();
  }, [words]);

  const renderWords = () => {
    return (
      <motion.div ref={scope}>
        {wordsWithLineBreaks.map((word, idx) => {
          if (word === "\n") {
            return <br key={`br-${idx}`} />;
          }
          
          return (
            <motion.span
              key={`${word}-${idx}`}
              className="dark:text-white text-black opacity-0"
              style={{
                filter: filter ? "blur(10px)" : "none",
              }}
            >
              {word}{" "}
            </motion.span>
          );
        })}
      </motion.div>
    );
  };

  return (
    <div className={cn("font-semibold", className)}>
      <div className="mt-4">
        <div className="dark:text-white text-black text-md leading-snug tracking-wide">
          {renderWords()}
        </div>
      </div>
    </div>
  );
};