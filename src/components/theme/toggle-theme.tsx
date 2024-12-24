"use client";
import { Moon, Sun } from 'lucide-react';
import { useTheme } from "next-themes";
import { Button } from "../ui/button";
import { useEffect, useState } from "react";


export function ToggleTheme(){
  const [mounted, setIsMounted] = useState<boolean>(false); 
  const {setTheme, theme} = useTheme();
  useEffect(()=>{
    setIsMounted(true);
  },[]);

  if(!mounted){
    return null;
  }
  
  return(
    <Button
  onClick={() => {
    (() => (theme === "dark" ? setTheme("light") : setTheme("dark")))();
    }}
    className="absolute right-4 top-4"
  >
    {theme === "dark" ? <Sun /> : <Moon />}
  </Button>
  )
}