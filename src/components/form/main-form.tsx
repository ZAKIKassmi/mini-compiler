"use client";

import { useForm } from "react-hook-form";
import { Form, FormControl, FormField, FormItem } from "../ui/form";
import { Button } from "../ui/button";
import { ExternalLink, SendHorizontal, X } from "lucide-react";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "../ui/select";
import { getURL } from "@/utils/getURL";
import axios from "axios";
import { useToast } from "@/hooks/use-toast";
import { useEffect, useState } from "react";
import { Textarea } from "../ui/textarea";
import { TextGenerateEffect } from "../ui/text-generate-effect";
import { ScrollArea } from "../ui/scroll-area";
import { motion, AnimatePresence } from "framer-motion";

import InfoDrawer from "../custom/info-drawer";

type DataType = {
  value: string;
  selectValue: String;
  language: "fr" | "en";
  theme: string;
};

type responseType = {
  is_error: boolean;
  message: string;
  bayt: string;
};

export function MainForm() {
  const { toast } = useToast();
  const [value, setValue] = useState("1");
  const [theme, setTheme] = useState("1");
  const [isTranslationVisible, setIsTranslationVisible] =
    useState<boolean>(false);
  const [translationContent, setTranslationContent] = useState<string>("");
  const [showAnimation, setShowAnimation] = useState(false);
  const [closestMatch, setClosesMatch] = useState(null);
  const [isOk, setIsOk] = useState(false);
  const [isSuggestion, setIsSuggestion] = useState(false);

  useEffect(() => {
    const isTranslation = value === "2";
    const isSuggestion = value === "3";
    setIsSuggestion(isSuggestion);
    setIsTranslationVisible(isTranslation);
    if (!isTranslation) {
      setShowAnimation(false);
      setTranslationContent("");
      setClosesMatch(null);
    }
    setIsOk(false);
  }, [value]);

  const form = useForm<DataType>({
    defaultValues: {
      value: "",
      selectValue: "1",
      language: "en",
      theme: "1"
    },
  });

  async function onSubmit(input: DataType) {
    const value = input.value;
    const selectValue = input.selectValue;
    const language = input.language;
    const URL = getURL();

    switch (selectValue) {
      case "1":
        const { data }: { data: responseType } = await axios.post(
          `${URL}/py/verify_input`,
          {
            proverb_input: value,
          }
        );

        if (data.is_error) {
          toast({
            title: data.message,
            description: `Found in: ${data.bayt}`,
            variant: "destructive",
          });
          setIsOk(false);
        } else {
          toast({
            title: data.message,
            description: data.bayt,
            variant: "default",
          });
          setIsOk(true);
        }
        break;
      case "2":
        try {
          const { data } = await axios.post(`${URL}/py/translation`, {
            input: value,
            translate_to: language,
          });
          if (data.is_error) {
            setIsOk(false);
            toast({
              title: data.translation,
              variant: "destructive",
              description: `Found: ${data.bayt}`,
            });
            if (data.closest_match.length > 0) {
              setClosesMatch(data.closest_match);
            }
          } else {
            setIsOk(true);
            setClosesMatch(null);
            setTranslationContent(data.translation);
            setShowAnimation(false);
            requestAnimationFrame(() => setShowAnimation(true));
          }
        } catch (e) {
          toast({
            title: `${e}`,
            variant: "destructive",
          });
        }
        break;

      case "3":
        break;

      default:
        console.log("Hehe");
    }
  }

  return (
    <>
      <div className="max-w-[30rem] w-full flex flex-col gap-4">
        <Form {...form}>
          <motion.form
            layout
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.3 }}
            onSubmit={form.handleSubmit(onSubmit)}
            className="flex items-center gap-2 flex-col w-full"
          >
            <AnimatePresence mode="wait">
              {!isSuggestion && (
                <motion.div
                  key="textarea"
                  layout
                  initial={{ opacity: 0, height: 0 }}
                  animate={{ opacity: 1, height: 'auto' }}
                  exit={{ opacity: 0, height: 0 }}
                  transition={{ duration: 0.3 }}
                  className="w-full"
                >
                  <FormField
                    control={form.control}
                    name="value"
                    render={({ field }) => (
                      <FormItem className="w-full">
                        <FormControl>
                          <Textarea
                            rows={6}
                            placeholder="Anything in your mind?"
                            {...field}
                          />
                        </FormControl>
                      </FormItem>
                    )}
                  />
                </motion.div>
              )}
            </AnimatePresence>

            <div className="flex w-full gap-2">
              <FormField
                control={form.control}
                name="selectValue"
                render={({ field }) => (
                  <FormItem className="w-full">
                    <Select
                      onValueChange={(e) => {
                        field.onChange(e);
                        setValue(e);
                      }}
                      value={value}
                    >
                      <FormControl>
                        <SelectTrigger className="w-full">
                          <SelectValue placeholder="Compiler" />
                        </SelectTrigger>
                      </FormControl>
                      <SelectContent>
                        <SelectItem value="1">Compiler</SelectItem>
                        <SelectItem value="2">Translator</SelectItem>
                        <SelectItem value="3">Suggestions</SelectItem>
                      </SelectContent>
                    </Select>
                  </FormItem>
                )}
              />

              <AnimatePresence mode="wait">
                {isTranslationVisible && (
                  <motion.div
                    key="language-select"
                    layout
                    
                  >
                    <FormField
                      control={form.control}
                      name="language"
                      render={({ field }) => (
                        <FormItem className="w-full">
                          <Select
                            onValueChange={field.onChange}
                            defaultValue={String(field.value)}
                          >
                            <FormControl>
                              <SelectTrigger className="w-36">
                                <SelectValue placeholder="English" />
                              </SelectTrigger>
                            </FormControl>
                            <SelectContent>
                              <SelectItem value="en">English</SelectItem>
                              <SelectItem value="fr">French</SelectItem>
                            </SelectContent>
                          </Select>
                        </FormItem>
                      )}
                    />
                  </motion.div>
                )}
              </AnimatePresence>

              <AnimatePresence mode="wait">
                {isSuggestion && (
                  <motion.div
                    key="theme-select"
                    layout
                  >
                    <FormField
                      control={form.control}
                      name="theme"
                      render={({ field }) => (
                        <FormItem className="w-full">
                          <Select
                            onValueChange={(e) => {
                              field.onChange(e);
                              setTheme(e);
                            }}
                            value={theme}
                          >
                            <FormControl>
                              <SelectTrigger className="w-36">
                                <SelectValue placeholder="الصبر" />
                              </SelectTrigger>
                            </FormControl>
                            <SelectContent>
                              <SelectItem value="1">الصبر</SelectItem>
                              <SelectItem value="2">الصداقة</SelectItem>
                              <SelectItem value="3">الحب</SelectItem>
                              <SelectItem value="4">الحرية</SelectItem>
                              <SelectItem value="5">جود وكرم</SelectItem>
                            </SelectContent>
                          </Select>
                        </FormItem>
                      )}
                    />
                  </motion.div>
                )}
              </AnimatePresence>

              <Button type="submit">
                <SendHorizontal />
              </Button>
            </div>
          </motion.form>
        </Form>

        <AnimatePresence>
          {closestMatch && isTranslationVisible && (
            <motion.div
              layout
              initial={{ opacity: 0, y: -20 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -20 }}
              transition={{ duration: 0.3 }}
              className="flex w-full justify-between text-sm"
            >
              <p>Closest match:</p>
              <p className="text-green-500">{closestMatch}</p>
            </motion.div>
          )}
        </AnimatePresence>

        <AnimatePresence>
          {isTranslationVisible && showAnimation && translationContent && (
            <motion.div
              layout
              initial={{ opacity: 0, x: 100 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: 100 }}
              transition={{ duration: 0.4, ease: "easeInOut" }}
              className="mt-4 absolute right-4 top-12 h-[90vh] w-[30%] dark:border-white/15 border rounded-xl p-4 dark:bg-[#121212] text-black/50 border-black/5 "
            >
              <ScrollArea className="w-full h-full">
                <TextGenerateEffect
                  duration={2}
                  filter={false}
                  words={translationContent}
                />
              </ScrollArea>
            </motion.div>
          )}
        </AnimatePresence>
      </div>

      <AnimatePresence>
        {isOk && (
          <motion.div
            layout
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            exit={{ opacity: 0, scale: 0.9 }}
            transition={{ duration: 0.3 }}
          >
            <InfoDrawer
              title="Abu at-Tayyib Ahmad ibn al-Husayn al-Mutanabbi al-Kindi"
              imageSrc="/moutanabi.jpg"
              imageAlt="moutananbu image"
              biographyLink="https://en.wikipedia.org/wiki/Al-Mutanabbi"
              biographyText="Abū al-Ṭayyib Aḥmad ibn al-Ḥusayn al-Mutanabbī al-Kindī from Kufa, Abbasid Caliphate, was a famous Abbasid-era Arabian poet at the court of the Hamdanid emir Sayf al-Dawla in Aleppo, and for whom he composed 300 folios of poetry."
              videoUrl="https://www.youtube.com/embed/SWgu48f2rxk"
              metadata={{
                born: "Kufa, Iraq",
                died: "September 23, 965 AD, Numaniyah, Iraq",
                era: "Islamic Golden Age",
              }}
            />
          </motion.div>
        )}
      </AnimatePresence>
    </>
  );
}
